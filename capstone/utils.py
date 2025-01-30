from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import get_object_or_404

from flight.models import *
import secrets
from datetime import datetime, timedelta
from xhtml2pdf import pisa

from flight.constant import FEE

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def createticket(user,passengers,passengerscount,flight1,flight_1date,flight_1class,coupon,countrycode,email,mobile):
    ticket = Ticket.objects.create()
    ticket.user = user
    ticket.ref_no = secrets.token_hex(3).upper()
    for passenger in passengers:
        ticket.passengers.add(passenger)
    ticket.flight = flight1
    ticket.flight_ddate = datetime(int(flight_1date.split('-')[2]),int(flight_1date.split('-')[1]),int(flight_1date.split('-')[0]))
    ###################
    flight1ddate = datetime(int(flight_1date.split('-')[2]),int(flight_1date.split('-')[1]),int(flight_1date.split('-')[0]),flight1.depart_time.hour,flight1.depart_time.minute)
    flight1adate = (flight1ddate + flight1.duration)
    ###################
    ticket.flight_adate = datetime(flight1adate.year,flight1adate.month,flight1adate.day)
    ffre = 0.0
    if flight_1class.lower() == 'first':
        ticket.flight_fare = flight1.first_fare*int(passengerscount)
        ffre = flight1.first_fare*int(passengerscount)
    elif flight_1class.lower() == 'business':
        ticket.flight_fare = flight1.business_fare*int(passengerscount)
        ffre = flight1.business_fare*int(passengerscount)
    else:
        ticket.flight_fare = flight1.economy_fare*int(passengerscount)
        ffre = flight1.economy_fare*int(passengerscount)
    ticket.other_charges = FEE
    if coupon:
        ticket.coupon_used = coupon                     ##########Coupon
    ticket.total_fare = ffre+FEE+0.0                    ##########Total(Including coupon)
    ticket.seat_class = flight_1class.lower()
    ticket.status = 'PENDING'
    ticket.mobile = ('+'+countrycode+' '+mobile)
    ticket.email = email
    ticket.save()
    return ticket

def createHotelReceipts(user, hotel_booking,countrycode, email, mobile):
    """
    Generates a receipt for hotel bookings.
    """
    # Create a new receipt object
    # receipt = HotelReceipt.objects.create()
    # receipt.user = user
    # receipt.ref_no = secrets.token_hex(3).upper()

    # hotel_booking = get_object_or_404(HotelBooking, id=hotel_booking.id)
    # print("hotel_booking:  ",hotel_booking)
    # receipt.hotel = hotel_booking.hotel
    # receipt.checkin_date = hotel_booking.checkin_date
    # receipt.checkout_date = hotel_booking.checkout_date
    # receipt.room_type = hotel_booking.room_type
    # receipt.num_rooms = hotel_booking.num_rooms
    # receipt.booking_date = hotel_booking.booking_date
    # receipt.total_cost = hotel_booking.price
    # receipt.mobile = f"+{countrycode} {mobile}"
    # receipt.email = email

    # # Save the receipt
    # receipt.save()

    # Optionally render a PDF for the receipt
    # pdf_context = {
    #     "user": user,
    #     "hotel": hotel_booking.hotel,
    #     "checkin_date": hotel_booking.checkin_date,
    #     "checkout_date": hotel_booking.checkout_date,
    #     "room_type": hotel_booking.room_type,
    #     "num_rooms": hotel_booking.num_rooms,
    #     "total_cost": hotel_booking.price,
    #     "booking_date": hotel_booking.booking_date,
    #     "ref_no": receipt.ref_no,
    #     "mobile": receipt.mobile,
    #     "email": receipt.email,
    # }
    # pdf = render_to_pdf("flight/hotel_receipt.html", pdf_context)

    # Return the receipt and optionally the PDF
    # return receipt, pdf


    """
    Generates a receipt for hotel bookings.
    """
    # Create a new receipt object with all necessary fields
    hotel_booking = get_object_or_404(HotelBooking, id=hotel_booking.id)
    receipt = HotelReceipt.objects.create(
        user=user,
        ref_no=secrets.token_hex(3).upper(),
        hotel=hotel_booking.hotel,
        checkin_date=hotel_booking.checkin_date,
        checkout_date=hotel_booking.checkout_date,
        room_type=hotel_booking.room_type,
        num_rooms=hotel_booking.num_rooms,
        booking_date=hotel_booking.booking_date,
        total_cost=hotel_booking.price,
        mobile=f"+{countrycode} {mobile}",
        status="PENDING",
        email=email
    )

    return receipt
