from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse,JsonResponse

from django.views.decorators.csrf import csrf_exempt

from .models import FeeCategory, FeePayment, FeeReminder,Student
from .forms import FeeCategoryForm, FeeReminderForm,FeePaymentForm
from django.db.models import Count
from django.template.loader import get_template
from django.template import Context
# from reportlab.pdfgen import canvas
from io import BytesIO
import json
import requests
from django.urls import reverse


@csrf_exempt
def accountant_home(request):
    total_students = Student.objects.count()
    paid_students = FeePayment.objects.values('student').annotate(total=Count('student'))
    total_paid_students = len(paid_students)
    unpaid_students = total_students - total_paid_students
    context = {
        'total_students': total_students,
        'total_paid_students': total_paid_students,
        'unpaid_students': unpaid_students
    }
    return render(request, "accountant_template/home_content.html", context)

def fee_category_list(request):
    if request.method == 'POST' and 'delete_fee_category' in request.POST:
        fee_category_id = request.POST.get('delete_fee_category')
        FeeCategory.objects.filter(id=fee_category_id).delete()
        return redirect('fee_category_list')

    fee_categories = FeeCategory.objects.all()
    return render(request, 'accountant_template/fee_category_list.html', {'fee_categories': fee_categories})

def create_fee_category(request):
    if request.method == 'POST':
        form = FeeCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fee_category_list')
    else:
        form = FeeCategoryForm()
    return render(request, 'accountant_template/create_fee_category.html', {'form': form})

# def update_fee_category(request, pk):
#     fee_category = get_object_or_404(FeeCategory, pk=pk)
#     if request.method == 'POST':
#         form = FeeCategoryForm(request.POST, instance=fee_category)
#         if form.is_valid():
#             form.save()
#             return redirect('fee_category_list')
#     else:
#         form = FeeCategoryForm(instance=fee_category)
#     return render(request, 'update_fee_category.html', {'form': form})

def fee_payment_list(request):
    fee_payments = FeePayment.objects.all()
    return render(request, 'accountant_template/fee_payment_list.html')


def receive_fee(request):
    if request.method == 'POST':
        form = FeePaymentForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or render success message
            return redirect('generate_invoice_pdf')  # Redirect to invoice page after successful payment
    else:
        form = FeePaymentForm()
    return render(request, 'accountant_template/create_fee_payment.html', {'form': form})

def invoice(request):
    # Retrieve the latest fee payment record
    latest_payment = FeePayment.objects.latest('payment_date')
    return render(request, 'accountant_template/invoice.html', {'latest_payment': latest_payment})

def generate_invoice_pdf(request):
    latest_payment = FeePayment.objects.latest('payment_date')

    # Create a buffer to store PDF data
    buffer = BytesIO()

    # Create a canvas
    p = canvas.Canvas(buffer)

    # Draw the invoice content
    p.drawString(100, 570, f"Session: {latest_payment.session}")
    p.drawString(100, 710, f"Course: {latest_payment.course}")
    p.drawString(100, 690, f"Student: {latest_payment.student}")
    p.drawString(100, 660, f"Fee Category: {latest_payment.fee_category}")
    p.drawString(100, 630, f"Amount: {latest_payment.amount}")
    p.drawString(100, 600, f"Payment Date: {latest_payment.payment_date}")

    # Save the PDF
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and return the PDF as HttpResponse
    pdf_data = buffer.getvalue()
    buffer.close()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    response.write(pdf_data)
    return response
from django.shortcuts import render, get_object_or_404
from .models import FeePayment

def view_student_fee_payment(request, fee_payment_id):
    fee_payment = get_object_or_404(FeePayment, id=fee_payment_id)
    student = fee_payment.student  # Assuming there's a ForeignKey field named 'student' in FeePayment model
    return render(request, 'accountant_template/view_student_fee_payment.html', {'student': student, 'fee_payment': fee_payment})


def paid_fee_students(request):
    # Get all students who have made fee payments
    paid_students = []
    for fee_payment in FeePayment.objects.select_related('student').all():
        student = fee_payment.student
        paid_students.append({
            'student_id': student.id,
            'name': student.name,
            'payment_date': fee_payment.payment_date,
            'amount_paid': fee_payment.amount,
        })

    return render(request, 'accountant_template/paid_fee_students.html', {'paid_students': paid_students})



def fee_reminder_list(request):
    fee_reminders = FeeReminder.objects.all()
    return render(request, 'accountant_template/fee_reminder_list.html', {'fee_reminders': fee_reminders})

