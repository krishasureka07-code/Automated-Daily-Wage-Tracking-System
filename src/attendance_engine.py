# Handle attendance and payment
from storage import SHIFTS_FILE, load_data, save_data
from wage_calculator import compute_daily_wage
from datetime import datetime
from worker_manager import find_worker
def generate_shift_id(shifts):
    if not shifts:
        return "SFT-1001"
    last_id = shifts[-1]["shift_id"]
    number = int(last_id.split("-")[1]) + 1
    return "SFT-" + str(number)
def log_shift(worker_id, date, check_in, check_out):
    worker = find_worker(worker_id)
    if worker is None:
        return False, "Worker not found.", None
    if check_out <= check_in:
        return False, "Check-out time must be after check-in time.", None
    hours_worked = check_out - check_in
    if hours_worked > 20:
        return False, "Shift cannot be more than 20 hours.", None
    wage_details = compute_daily_wage(
        worker["daily_rate"], hours_worked= check_out-check_in
    )
    shifts = load_data(SHIFTS_FILE)
    shift_id = generate_shift_id(shifts)
    shift = {
        "shift_id": shift_id,
        "worker_id": worker["worker_id"],
        "name": worker["name"],
        "date": date.strip(),
        "check_in": check_in,
        "check_out": check_out,
        "check_in_time": f"{int(check_in):02d}:{int(round((check_in - int(check_in)) * 60)):02d}",
        "check_out_time": f"{int(check_out):02d}:{int(round((check_out - int(check_out)) * 60)):02d}",
        "hours_worked": round(hours_worked, 2),
        "breakdown": wage_details,
        "settlement_status": "UNPAID"
    }
    shifts.append(shift)
    save_data(SHIFTS_FILE, shifts)
    return True, "Shift logged with ID: " + shift_id, shift
def settle_shift_payment(shift_id):
    shifts = load_data(SHIFTS_FILE)
    shift_id = shift_id.strip().upper()
    for shift in shifts:
        if shift["shift_id"] == shift_id:
            if shift["settlement_status"] == "PAID":
                return False, "This shift is already paid."
            shift["settlement_status"] = "PAID"
            shift["paid_on"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            save_data(SHIFTS_FILE, shifts)
            return True, "Payment marked as PAID."
    return False, "Shift ID not found."