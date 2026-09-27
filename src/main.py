# Main program for wage tracking
import sys
from attendance_engine import log_shift, settle_shift_payment
from dashboard import generate_site_analytics
from storage import SHIFTS_FILE, load_data
from worker_manager import get_all_skills, register_worker
def show_menu():
    print("\n******** SHRAMIK SETU *******")
    print("1. Register Worker")
    print("2. Log Attendance")
    print("3. View Wage Slip")
    print("4. Settle Payment")
    print("5. View Payroll Analytics")
    print("6. View Skills")
    print("7. Exit")
def show_wage_slip(shift):
    b = shift["breakdown"]
    print("\n===== WAGE SLIP =====")
    print("Shift ID:", shift["shift_id"])
    print("Worker ID:", shift["worker_id"])
    print("Name:", shift["name"])
    print("Date:", shift["date"])
    print("Hours Worked:", shift["hours_worked"])
    print("\nRegular Hours:", b["regular_hours"])
    print("Regular Pay: Rs.", b["regular_pay"])
    print("Overtime Hours:", b["overtime_hours"])
    print("Overtime Pay: Rs.", b["overtime_pay"])
    print("Total Wage: Rs.", b["total_wage"])
    print("Payment Status:", shift["settlement_status"])
def register():
    name = input("Enter worker name: ")
    skill = input("Enter skill (Unskilled / Semi-Skilled / Skilled): ")
    rate = input("Enter daily wage: ")

    success, message = register_worker(name, skill, rate)
    print(message)
def log_attendance():
    worker_id = input("Enter Worker ID: ")
    date = input("Enter date (DD-MM-YYYY): ")
    try:
        check_in = float(input("Enter check-in time: "))
        check_out = float(input("Enter check-out time: "))
        success, message, shift = log_shift(
            worker_id, date, check_in, check_out
        )
        print(message)
        if success:
            show_wage_slip(shift)
    except ValueError:
        print("Please enter time using numbers like 8.0 or 17.5.")
def view_slip():
    shift_id = input("Enter Shift ID: ").strip().upper()

    shifts = load_data(SHIFTS_FILE)
    for shift in shifts:
        if shift["shift_id"] == shift_id:
            show_wage_slip(shift)
            return
    print("Shift ID not found.")
def settle_payment():
    shift_id = input("Enter Shift ID: ").strip().upper()
    success, message = settle_shift_payment(shift_id)
    print(message)
def view_skills():
    skills = get_all_skills()
    print("\nAvailable Skills:", skills)
def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            log_attendance()
        elif choice == "3":
            view_slip()
        elif choice == "4":
            settle_payment()
        elif choice == "5":
            print(generate_site_analytics())
        elif choice == "6":
            view_skills()
        elif choice == "7":
            print("Thank you for using ShramikSetu!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1 to 7.")
if __name__ == "__main__":
    main()

