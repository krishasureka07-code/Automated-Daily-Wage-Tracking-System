# Dashboard for wage trackinh
from storage import SHIFTS_FILE, WORKERS_FILE, load_data
def find_highest_overtime_worker():
    shifts = load_data(SHIFTS_FILE)
    if not shifts:
        return None
    highest = shifts[0]
    for shift in shifts:
        if shift["breakdown"]["overtime_hours"] > highest["breakdown"]["overtime_hours"]:
            highest = shift
    return highest
def generate_site_analytics():
    shifts = load_data(SHIFTS_FILE)
    workers = load_data(WORKERS_FILE)
    if not shifts:
        return "No shift records available."
    total_hours = 0
    overtime_hours = 0
    total_wages = 0
    unpaid_wages = 0
    for shift in shifts:
        total_hours += shift["hours_worked"]
        overtime_hours += shift["breakdown"]["overtime_hours"]
        total_wages += shift["breakdown"]["total_wage"]

        if shift["settlement_status"] == "UNPAID":
            unpaid_wages += shift["breakdown"]["total_wage"]
    highest = find_highest_overtime_worker()
    if highest and highest["breakdown"]["overtime_hours"] > 0:
        peak = (
            highest["name"] + " (" + highest["worker_id"] + ") - "
            + str(highest["breakdown"]["overtime_hours"])
            + " OT hours on " + highest["date"]
        )
    else:
        peak = "No overtime recorded"
    report = (
        "\n     SHRAMIK SETU DASHBOARD   \n"
        + "Total Workers: " + str(len(workers)) + "\n"
        + "Total Shifts: " + str(len(shifts)) + "\n"
        + "Total Hours: " + str(round(total_hours, 2)) + "\n"
        + "Total Overtime: " + str(round(overtime_hours, 2)) + "\n"
        + "Total Wages: Rs. " + str(round(total_wages, 2)) + "\n"
        + "Unpaid Wages: Rs. " + str(round(unpaid_wages, 2)) + "\n"
        + "Highest Overtime: " + peak
    )
    return report
