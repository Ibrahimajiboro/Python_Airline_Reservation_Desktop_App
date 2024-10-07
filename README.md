# ABC Airlines Booking System

## Overview
The ABC Airlines Booking System is a Python-based GUI application designed to handle user registration, flight reservation, and payment for ABC Airlines. It uses the `Tkinter` library for the graphical user interface and `SQLite` for data storage.

### Key Features:
- **User Registration:** New users can register with their personal details.
- **Login:** Existing users can log in using a username and password.
- **Flight Reservation:** Users can reserve flights by selecting departure, destination, class, and ticket type.
- **Payment Options:** Users can pay for reservations through various methods (Bank Transfer, Debit Card, and Online Payment).

---

## Prerequisites
To run the application, ensure the following libraries are installed:
1. Python 3.x
2. Tkinter (Standard Python library for GUI applications)
3. PIL (Python Imaging Library) for handling images
4. SQLite3 (Database included with Python)
5. `tkcalendar` for date selection
6. `ttk` (from Tkinter) for styling combobox widgets

You can install the required libraries using the following:
```bash
pip install pillow tk tkcalendar
```

---

## Database Structure
The application uses `SQLite3` to store user data and flight reservation information.

- **User Data (registerdata):**
  - firstname (Primary Key)
  - midname
  - surname
  - contact (Phone number)
  - email
  - nin (National Identification Number)
  - address
  - username
  - password

- **Reservation Data (reservationdata):**
  - firstname (Primary Key)
  - midname
  - surname
  - contact (Phone number)
  - email
  - address
  - class (e.g., economy, standard, first class)
  - ticket (single or return)
  - age (child or adult)
  - departure
  - destination
  - date (flight date)
  - time (flight time)
  - amount (calculated ticket price)

---

## Application Flow

### 1. **Login Page:**
The application starts at the login page where users must enter their username and password. If they do not have an account, they can register by clicking on the "Sign Up" button.

### 2. **Registration Page:**
Users input personal details such as name, contact, email, NIN, and set up a username and password. These details are saved to the `registerdata` table in the SQLite database.

### 3. **Reservation Page:**
Once logged in, users can reserve a flight by selecting:
- **Personal Information:** First name, last name, and phone number.
- **Ticket Details:** Class, type (single or return), age group.
- **Flight Details:** Departure and destination, date, and time.
- **Summary and Confirmation:** A billing page shows the reservation summary before final confirmation.

### 4. **Payment Page:**
On the payment page, users can choose between three payment methods:
- **Bank Transfer:** Displays bank details for transferring the payment.
- **Debit Card:** Allows the user to enter card details and verify with OTP.
- **3D Online Payment:** Provides a link to an external payment gateway.

---

## How to Run

1. Clone the repository or download the source files.
2. Ensure that all required dependencies are installed.
3. Run the `main.py` (or equivalent) file to start the application.

```bash
python main.py
```

The application will launch the login page as the entry point.

---

## Files in the Project
- **main.py**: The entry point of the application.
- **images/**: Contains the image assets used for GUI (e.g., airplane images).
- **database/**: Stores the `testcode.db` SQLite database file for storing user and reservation data.

---

## Future Improvements
- Enhance security measures for password storage (e.g., password hashing).
- Add support for international destinations.
- Improve the payment verification process.

---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
