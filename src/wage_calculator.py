# To calculate daily wage
def compute_daily_wage(daily_rate, hours_worked):
    if daily_rate <= 0 or hours_worked <= 0:
        return {
            "regular_hours": 0,
            "overtime_hours": 0,
            "regular_pay": 0,
            "overtime_pay": 0,
            "total_wage": 0
        }
    hourly_rate = daily_rate / 8
    if hours_worked <= 8:
        regular_hours = hours_worked
        overtime_hours = 0
    else:
        regular_hours = 8
        overtime_hours = hours_worked - 8
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    total_wage = regular_pay + overtime_pay
    return {
        "regular_hours": regular_hours,
        "overtime_hours": overtime_hours,
        "regular_pay": round(regular_pay, 2),
        "overtime_pay": round(overtime_pay, 2),
        "total_wage": round(total_wage, 2)
    }