from celery import shared_task
from django.core.mail import send_mail
from datetime import datetime

@shared_task
def send_booking_confirmation_email(to_email, booking_id):
    """
    Sends booking confirmation email asynchronously.
    """
    subject = f"Booking Confirmation #{booking_id}"
    message = f"Your booking with ID {booking_id} has been confirmed!"
    from_email = "noreply@alxtravelapp.com"
    send_mail(subject, message, from_email, [to_email])

    log_message = f"{datetime.now()} - Email sent to {to_email} for booking {booking_id}\n"
    with open('/tmp/booking_email_log.txt', 'a') as log_file:
        log_file.write(log_message)

    return f"Email sent to {to_email}"
  
