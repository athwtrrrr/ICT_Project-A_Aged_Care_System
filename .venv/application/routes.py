from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from application import get_db
from application.auth import has_permission  # Correct import for shared helper

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/')
@routes_bp.route('/index')
@routes_bp.route('/home')
def index():
    return render_template('index.html', home=True)

@routes_bp.route('/admin_dashboardresident')
def admin_dashboardresident():
    if not has_permission('manage_users'):
        return redirect(url_for('auth.login'))
    return render_template('admin_dashboardresident.html', admin_dashboardresident=True)


@routes_bp.route('/admin_staff_directory')
def admin_staff_directory():
    if not has_permission('manage_users'):
        return redirect(url_for('auth.login'))
    return render_template('admin_staff_directory.html', admin_staff_directory=True)

@routes_bp.route('/staff_directory')
def staff_directory():
    if not has_permission('view_staff_directory'):
        return redirect(url_for('auth.login'))
    return render_template('staff_directory.html', staff_directory=True)

@routes_bp.route('/services')
def services():
    if not has_permission('view_services'):
        return redirect(url_for('auth.login'))
    return render_template('services.html', services=True)

@routes_bp.route('/inventory')
def inventory():
    if not has_permission('manage_inventory'):
        return redirect(url_for('auth.login'))
    return render_template('inventory.html', inventory=True)

@routes_bp.route('/family_portalresident')
def family_portalresident():
    if not has_permission('view_family_portalresidents'):
        return redirect(url_for('auth.login'))
    return render_template('family_portalresident.html', family_portalresident=True)

@routes_bp.route('/booking')
def booking():
    if not has_permission('view_family_portalresidents'):
        return redirect(url_for('auth.login'))
    return render_template('booking.html', booking=True)

@routes_bp.route('/logout')
def logout():
    # Clear the user session
    session.clear()
    # Flash a logout message
    flash('You have been successfully logged out', 'success')
    # Redirect to login page or home page
    return redirect(url_for('auth.login'))  # or 'routes.index' if you prefer