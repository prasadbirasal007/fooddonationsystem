# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from models import init_db, add_donation, get_all_donations, delete_donation

app = Flask(__name__)
app.secret_key = 'dev-secret-key'  # change for production

# initialize db helper (will raise if DB not reachable)
init_db()

@app.route('/')
def index():
    donations = get_all_donations()
    return render_template('index.html', donations=donations)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        donor_name = request.form.get('donor_name')
        contact = request.form.get('contact')
        quantity = request.form.get('quantity')
        pickup_address = request.form.get('pickup_address')
        notes = request.form.get('notes')

        if not donor_name or not quantity:
            flash('Name and quantity are required.')
            return redirect(url_for('add'))

        inserted = add_donation(donor_name, contact, quantity, pickup_address, notes)
        flash(f'Donation added (id={inserted})')
        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/delete/<int:donation_id>', methods=['POST'])
def delete(donation_id):
    success = delete_donation(donation_id)
    if success:
        flash(f'Deleted donation id={donation_id}')
    else:
        flash(f'No donation found with id={donation_id}')
    return redirect(url_for('index'))

if __name__ == '__main__':
    # debug=True will auto-reload templates on change; still restart if you changed python files
    app.run(debug=True)
