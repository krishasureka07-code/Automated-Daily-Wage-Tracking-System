# Shramik Setu - Daily Wage Tracking GUI

## Run

From the folder containing `app.py`:

```powershell
py app.py
```

## Main tabs

- **Dashboard** - active workers, shifts, hours, wages, unpaid wages, overtime and skill summary.
- **Workers** - register workers, automatic skill classification and unregister workers.
- **Attendance** - record a worker's shift using normal clock times such as `08:00` and `17:30`.
- **Shifts** - complete shift register showing Worker ID, Worker Name, Shift ID, Date, Check In, Check Out, Hours, Wage and Payment Status.
- **Payments & Records** - review wage/payment records, filter/search them, mark an unpaid shift as PAID, export records, and clear the attendance log with confirmation.
- **All Workers** - complete active and historical worker register with search/filter and CSV export.

## Payment workflow

A newly recorded shift starts as **UNPAID**. In **Payments & Records**, select the record and click **Mark Selected as PAID**. The payment status and paid date/time are saved to `data/shifts.json`, and the Dashboard unpaid amount updates immediately.

## Data files

- `data/workers.json` - active workers
- `data/worker_history.json` - complete worker history
- `data/shifts.json` - shifts, wage calculations and payment status

The GUI no longer uses wage slips. Shift information is managed in the **Shifts** tab and payment information is managed in **Payments & Records**.
