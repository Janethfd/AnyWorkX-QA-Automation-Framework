Test Plan: AnyWorkX Customer Onboarding & Vendor Booking

Objective: To validate the end-to-end flow from user registration (Social & Regular) to successful vendor booking.

Scope:

Functional: Verification of OTP delivery (SMS for Nigeria, Email for International).

Security: Validation of KYC Tier 1 through Tier 4.

UI/UX: Responsive navigation of the "Explore" feature.

Test Scenarios:
| ID | Scenario | Priority | Expected Result |
| :--- | :--- | :--- | :--- |
| TC-01 | Regular Signup with valid data | High | User receives OTP and reaches Dashboard. |
| TC-02 | Social Login (Google/Apple) | High | Account auto-populates data from provider. |
| TC-03 | Booking a Vendor (Active < 3) | Critical | Booking request sent; "Book Now" disabled after 3 active. |
| TC-04 | KYC Tier 1 Upload | High | System triggers AI-face matching logic. |
