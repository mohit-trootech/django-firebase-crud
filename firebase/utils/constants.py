from enum import Enum


class Templates(Enum):
    ADD = "firebase/add_employee.html"
    HOME = "firebase/employee.html"


class Employees(Enum):
    STATUS_CHOICES = (
        ("active", "Active"),
        ("inactive", "Inactive"),
    )
    POSITION_CHOICES = (
        ("accountant", "Accountant"),
        ("ceo", "Chief Executive Officer (CEO)"),
        ("technical_author", "Technical Author"),
        ("software_engineer", "Software Engineer"),
        ("integration_specialist", "Integration Specialist"),
        ("pre_sales_support", "Pre-Sales Support"),
        ("sales_assistant", "Sales Assistant"),
        ("developer", "Developer"),
    )


class Urls(Enum):
    HOME_REVERSE = "index"
    ADD_EMPLOYEE_REVERSE = "add-employee"
    LOGIN_REVERSE = "login"


class Constants(Enum):
    NOT_AUTHENTICATED = "Please Login to Continue"
