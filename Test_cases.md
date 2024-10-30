# Test Execution Plan

## Prioritized Functional Test Cases

### A. Input Validation

| Test Case ID | Title                       | Description                                                          | Preconditions                    | Test Steps                                                       | Expected Result                                                 | Actual Result | Status | Comments |
|---------------|-----------------------------|----------------------------------------------------------------------|----------------------------------|------------------------------------------------------------------|---------------------------------------------------------------|---------------|--------|----------|
| **TC01**      | Checkout Form Validation    | Verify required fields (name, address) display error messages if left empty. | User is on the checkout page.    | 1. Leave name and address fields empty.<br>2. Click "Submit".   | Error messages are displayed for both fields.                 |               |        |          |
| **TC02**      | Field Format Checks         | Ensure incorrect formats (e.g., numbers in name fields) trigger validation. | User is on the checkout page.    | 1. Enter numbers in the name field.<br>2. Click "Submit".       | An error message is displayed indicating invalid input.        |               |        |          |
| **TC03**      | Input Validation for Checkout Fields | Ensure the checkout process rejects invalid formats (e.g., numbers) in first and last name fields. | User is on the checkout page.    | 1. Navigate to the cart page.<br>2. Click on "Checkout".<br>3. Enter numerical values in first and last name fields.<br>4. Enter a valid or invalid postcode.<br>5. Attempt to proceed with checkout. | An error message is displayed for invalid input.              |               |        |          |

### B. Boundary Testing

| Test Case ID | Title                       | Description                                                          | Preconditions                    | Test Steps                                                       | Expected Result                                                 | Actual Result | Status | Comments |
|---------------|-----------------------------|----------------------------------------------------------------------|----------------------------------|------------------------------------------------------------------|---------------------------------------------------------------|---------------|--------|----------|
| **TC04**      | Cart Quantity Limits        | Test min/max allowable quantities in the cart.                      | User is logged in and on product page. | 1. Add item to cart with quantity 0.<br>2. Add item with quantity above maximum. | The system should prevent adding items outside limits.       |               |        |          |
| **TC05**      | Character Limit on Fields   | Verify character limits in fields like name and address.            | User is on the checkout page.    | 1. Enter a name longer than the character limit.<br>2. Click "Submit". | An error message is displayed for exceeding limit.           |               |        |          |

### C. User Flow Tests

| Test Case ID | Title                       | Description                                                          | Preconditions                    | Test Steps                                                       | Expected Result                                                 | Actual Result | Status | Comments |
|---------------|-----------------------------|----------------------------------------------------------------------|----------------------------------|------------------------------------------------------------------|---------------------------------------------------------------|---------------|--------|----------|
| **TC06**      | Login Flow                  | Test login success and failure scenarios for each user type.        | User is on the login page.       | 1. Enter valid credentials and submit.<br>2. Enter invalid credentials and submit. | User successfully logs in or receives an error message.       |               |        |          |
| **TC07**      | Product to Checkout Flow    | End-to-end test from login through adding items to cart and completing checkout. | User is logged in.                | 1. Add items to cart.<br>2. Navigate to checkout.<br>3. Complete checkout process. | Order confirmation is received after checkout.               |               |        |          |
| **Performance Testing for TC07** | Performance of User Flow       | Evaluate the checkout process under load to identify bottlenecks. | User is logged in with multiple items in the cart. | 1. Simulate multiple users performing checkout simultaneously.<br>2. Measure response times and resource usage. | The system handles the load efficiently without significant slowdowns or errors. |               |        |          |

### D. Session Management

| Test Case ID | Title                       | Description                                                          | Preconditions                    | Test Steps                                                       | Expected Result                                                 | Actual Result | Status | Comments |
|---------------|-----------------------------|----------------------------------------------------------------------|----------------------------------|------------------------------------------------------------------|---------------------------------------------------------------|---------------|--------|----------|
| **TC08**      | Session Persistence         | Ensure users remain logged in during the session.                   | User is logged in.               | 1. Navigate to different pages.<br>2. Refresh the page.         | User remains logged in and can navigate without re-entering credentials. |               |        |          |
| **TC09**      | Logout Functionality        | Verify that logout removes session data and redirects to login.     | User is logged in.               | 1. Click the "Logout" button.                                   | User is redirected to the login page and session data is cleared. |               |        |          |

### E. Navigation and Redirects

| Test Case ID | Title                       | Description                                                          | Preconditions                    | Test Steps                                                       | Expected Result                                                 | Actual Result | Status | Comments |
|---------------|-----------------------------|----------------------------------------------------------------------|----------------------------------|------------------------------------------------------------------|---------------------------------------------------------------|---------------|--------|----------|
| **TC10**      | Menu Links (About, Logout) | Test each menu item redirects to the correct page.                  | User is logged in.               | 1. Click on each menu item.<br>2. Verify redirection.           | Each menu item redirects to the correct page.                 |               |        |          |
| **TC11**      | Continue Shopping Button     | Verify that “Continue Shopping” returns users to product page.     | User is on the cart page.        | 1. Click the "Continue Shopping" button.                        | User is returned to the product page.                         |               |        |          |

### F. Cart Management

| Test Case ID | Title                       | Description                                                          | Preconditions                    | Test Steps                                                       | Expected Result                                                 | Actual Result | Status | Comments |
|---------------|-----------------------------|----------------------------------------------------------------------|----------------------------------|------------------------------------------------------------------|---------------------------------------------------------------|---------------|--------|----------|
| **TC12**      | Add/Remove Items           | Confirm items can be added and removed correctly.                  | User is logged in and on product page. | 1. Add an item to the cart.<br>2. Remove the item.             | Item is successfully added and removed from the cart.         |               |        |          |
| **TC13**      | Empty Cart Behavior        | Test emptying the cart to ensure no errors when proceeding to checkout with an empty cart. | User is logged in.               | 1. Remove all items from the cart.<br>2. Click "Checkout".     | User can proceed to checkout without errors.                 |               |        |          |
| **TC14**      | Unable to Change Quantity   | Verify users can modify the quantity of items in the cart.         | User is logged in.               | 1. Add a product to the cart.<br>2. Navigate to the cart page.<br>3. Attempt to change quantity. | Users should be able to modify the quantity.                  |               |        |          |

### G. Error Messaging

| Test Case ID | Title                       | Description                                                          | Preconditions                    | Test Steps                                                       | Expected Result                                                 | Actual Result | Status | Comments |
|---------------|-----------------------------|----------------------------------------------------------------------|----------------------------------|------------------------------------------------------------------|---------------------------------------------------------------|---------------|--------|----------|
| **TC15**      | Login Error Messages        | Verify that incorrect logins display appropriate error messages.    | User is on the login page.       | 1. Enter invalid login credentials and submit.                 | An appropriate error message is displayed.                    |               |        |          |
| **TC16**      | Form Validation Errors      | Check that missing or incorrect inputs trigger correct error messages. | User is on the checkout page.    | 1. Leave required fields empty.<br>2. Click "Submit".          | Error messages are displayed for missing inputs.              |               |        |          |

### H. User Experience (UX) Testing

| Test Case ID | Title                       | Description                                                          | Preconditions                    | Test Steps                                                       | Expected Result                                                 | Actual Result | Status | Comments |
|---------------|-----------------------------|----------------------------------------------------------------------|----------------------------------|------------------------------------------------------------------|---------------------------------------------------------------|---------------|--------|----------|
| **TC17**      | Usability Testing           | Evaluate ease of navigation and understanding of the user interface. | User is on the homepage.         | 1. Navigate through various sections of the site.<br>2. Evaluate the clarity of buttons and information. | Users can navigate easily, and information is clear and understandable. |               |        |          |
| **TC18**      | Accessibility Testing       | Ensure the website is accessible to users with disabilities.       | User is on the homepage.         | 1. Use screen readers to navigate.<br>2. Check color contrast and alt text for images. | The website meets accessibility standards and is usable for all users. |               |        |          |
| **TC19**      | Aesthetic Review            | Assess the visual appeal of the site and consistency in design.    | User is on the homepage.         | 1. Evaluate overall look and feel, including fonts and colors. | The website is visually appealing and follows design guidelines. |               |        |          |


