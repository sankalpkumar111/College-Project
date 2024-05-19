EduLink-Integrated College Management and Communication System 
# College Enterprise Resource Planner

Welcome to the College Enterprise Resource Planner! This project was developed by me and my project partners for our college using Python/Django Framework. This fully functional web application aims to streamline various administrative and academic processes within the college environment.

## Features

### Admin Users Can:
- View overall summary charts of student performances, staff performances, courses, subjects, leave, etc.
- Manage staff (add, update, and delete)
- Manage students (add, update, and delete)
- Manage courses (add, update, and delete)
- Manage subjects (add, update, and delete)
- Manage sessions (add, update, and delete)
- Review and reply to student/staff feedback
- Review (approve/reject) student/staff leave requests

### Staff/Teachers Can:
- View overall summary charts related to their students, subjects, leave status, etc.
- Take/update student attendance
- Add/update student results
- Apply for leave
- Send feedback to HOD

### Students Can:
- View overall summary charts related to their attendance, subjects, leave status, etc.
- View attendance
- View results
- Apply for leave
- Send feedback to HOD

### Accountant Can:
- View overall summary of fee-related information
- Manage fee categories (add, update, delete)
- View fee payments
- Receive fee payments
- Generate invoices in PDF format
- View individual student fee payments
- View list of students who have paid fees
- Manage fee reminders





### Pre-Requisites:
- Install Git Version Control [https://git-scm.com/]
- Install Python Latest Version [https://www.python.org/downloads/]
- Install Pip (Package Manager) [https://pip.pypa.io/en/stable/installing/]

### Installation Steps:
1. **Clone the Project**:
   - Open your terminal or command prompt.
   - Navigate to the directory where you want to save the project.
   - Run the following command to clone the project repository:
     ```
     git clone https://github.com/sankalpkumar111/College-Project.git
     ```
2. **Create and Activate a Virtual Environment**:
   - Navigate into the project directory:
     ```
     cd College-Project
     ```
   - Create a virtual environment. Use one of the following commands based on your operating system:
     ```
     # For Windows
     python -m venv venv

     # For Mac/Linux
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     ```
     # For Windows
     venv\Scripts\activate

     # For Mac/Linux
     source venv/bin/activate
     ```

3. **Install Requirements**:
   - While in the virtual environment, install the project dependencies from the `requirements.txt` file:
     ```
     pip install -r requirements.txt
     ```

4. **Update Settings**:
   - Navigate to the `settings.py` file in the `EduLink` directory.
   - Update the `ALLOWED_HOSTS` setting with the appropriate host information.

5. **Run the Server**:
   - Run the Django development server with the following command:
     ```
     python manage.py runserver
     ```
   - The server will start running locally at `http://127.0.0.1:8000/`.

6. **Create Superuser (HOD)**:
   - To access the admin panel, create a superuser account by running the following command and following the prompts:
     ```
     python manage.py createsuperuser
     ```

### Project Usage:
- Access the project by navigating to `http://127.0.0.1:8000/` in your web browser.
- Log in with the credentials you created for the superuser.
- Explore and utilize the different features of the EduLink Integrated College Management and Communication System according to your role (admin, staff/teacher, student, accountant).

That's it! You've successfully installed and set up the EduLink Integrated College Management and Communication System project on your local machine. If you encounter any issues or need further assistance, feel free to ask!

### Login Credentials:
- Create super user (HOD) to access the admin panel.

## Project's Journey

This project has gone through various stages of development and improvement. Some of the key milestones include:
- Admin/Staff/Student/Accountant login functionality
- CRUD operations for course, staff, student, subject
- Profile management for admin, staff, student
- Attendance management
- Result management
- Leave application and approval
- Feedback system
- Integration of Google CAPTCHA
- Dynamic links and code restructuring for improved functionality
Certainly! Here's a condensed version:

### Project Journey Overview:

The EduLink project aimed to streamline college administration and communication. It progressed through key stages:

1. **Inception**: 
   - Researched college needs.
2. **Planning and Design**: 
   - Defined architecture and features.
3. **Development Kickoff**: 
   - Built core functionalities.
4. **Feature Development**: 
   - Iteratively added features like user management, attendance tracking, etc.
5. **User Testing and Feedback**: 
   - Gathered feedback to refine the system.
6. **Optimization and Deployment**: 
   - Enhanced performance and deployed to production.
7. **Documentation and Training**: 
   - Created guides and conducted training sessions.
8. **Continuous Improvement**: 
   - Continued updates based on feedback and evolving needs.

### Future Roadmap:

- Integration with specialized modules.
- UX/UI enhancements.
- Advanced analytics and reporting.
- Expanded communication channels.
- Adoption of emerging technologies for further improvements.

  Certainly! Here's a concise version:

### Support Developer:

Supporting the developer is crucial for the continued improvement and sustainability of the EduLink project. Here's how you can contribute:

- **Star the Repository**: Show your appreciation by starring the project repository.
- **Follow on GitHub & LinkedIn**: Stay updated with the latest developments and connect with the developer.
  
Your support motivates the developer to maintain and enhance the project, ensuring its usefulness and effectiveness for colleges worldwide.
## Contributors

- Sankalp kumar

