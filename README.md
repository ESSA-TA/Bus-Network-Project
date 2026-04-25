# Bus Network Project - Premium Transit 🚍

[cite_start]This is an advanced Django-based web application for managing bus routes and bookings, built as an extension of the airport example from the CS50 Web Lab[cite: 5, 6].

## Features
- [cite_start]**Route Management**: Users can view a comprehensive list of all available bus routes on the index page[cite: 31].
- [cite_start]**User Authentication**: Integrated Django’s built-in User model for secure registration, login, and logout functionality[cite: 12, 17, 26].
- [cite_start]**Booking Logic**: Logged-in users can book or unbook seats on specific routes through secure POST requests[cite: 33, 36, 38].
- [cite_start]**Route Details**: A detailed view for each route showing its origin, destination, duration, and the full list of booked passengers[cite: 32].
- **Form Validation**: Utilized `forms.py` to ensure clean architecture and robust validation for user-submitted data.

## Bonus Features (+15% points) 🌟
[cite_start]I have successfully implemented all the optional bonus features requested in the lab[cite: 42]:
- [cite_start]**My Routes Page**: A personalized dashboard for logged-in users to view all the routes they have booked[cite: 43].
- [cite_start]**Station Detail Page**: Detailed information for each station, listing all arriving and departing routes[cite: 44].
- [cite_start]**Search & Filter**: An efficient search functionality allowing users to filter routes by origin or destination[cite: 45].
- [cite_start]**Passenger Count**: Real-time display of the number of passengers next to each route on the index page[cite: 46].
- [cite_start]**Polished UI**: Fully styled with Bootstrap to provide a professional, responsive, and user-friendly experience[cite: 47].

## Technical Stack
- [cite_start]**Backend**: Django framework[cite: 14].
- [cite_start]**Database**: PostgreSQL used for production deployment[cite: 41, 106].
- [cite_start]**Static Files Management**: Configured with WhiteNoise for efficient delivery of CSS and JS in production[cite: 41, 145].
- [cite_start]**Deployment**: Live and accessible via a public URL on Railway[cite: 40].

## How to Use
1. Visit the live URL.
2. [cite_start]**Register**: Create a new account using the registration page[cite: 27].
3. [cite_start]**Login**: Access your account to enable booking features[cite: 28].
4. **Browse & Search**: Use the search bar to find specific routes or explore stations.
5. [cite_start]**Book a Seat**: Navigate to a route's detail page and click "Book" to reserve your seat[cite: 33].
6. [cite_start]**Manage Bookings**: View your reserved seats in the "My Routes" section or unbook them if needed[cite: 37].
