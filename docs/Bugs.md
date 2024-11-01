# Bug Report

## Summary of Issues

### Critical Issues
- **Input Validation for Checkout Fields**
  - **Description**: The checkout process accepts invalid formats for first name and last name fields (e.g., numbers).
  - **Steps to Reproduce**:
    1. Navigate to the cart page.
    2. Click on the "Checkout" button.
    3. Enter numerical values in the first name and last name fields.
    4. Enter a valid or invalid postcode.
    5. Attempt to proceed with the checkout.
  - **Expected Result**: The application should validate the inputs and reject numerical entries in the first name and last name fields, prompting an error message.
  - **Actual Result**: The application allows submission with numerical entries without any error messages.
  - **Severity**: Major

- **Unable to Change Quantity in Cart**
  - **Description**: Users are unable to modify the quantity of items in the cart. The quantity is fixed at 1 for all products.
  - **Steps to Reproduce**:
    1. Add any product to the cart.
    2. Navigate to the cart page.
    3. Attempt to change the quantity using the quantity input field (if available).
  - **Expected Result**: Users should be able to modify the quantity of the selected item, with the total price updating accordingly.
  - **Actual Result**: The quantity remains fixed at 1, and users are unable to make any adjustments.
  - **Severity**: Major

### Significant Issues
- **Loading Times/Performance Issues**
  - **Description**: For the user type `performance_glitch_user`, there was a noticeable delay in loading time, taking a few seconds longer than expected, which may indicate potential performance concerns that could affect user experience.
  
- **Menu Navigation - About Page**
  - **Description**: The link to the About page is broken, leading to an error page, requiring immediate attention.

### Moderate Issues
- **Password Visibility Icon Issue**
  - **Description**: After entering an incorrect password, the "show password" icon disappears upon displaying the error message.
  - **Steps to Reproduce**:
    1. Enter a valid username.
    2. Input an incorrect password.
    3. Submit the login form.
  - **Expected Behavior**: The "show password" icon should remain visible after an incorrect password entry.
  - **Actual Behavior**: The icon disappears, only reappearing once the password field is cleared.
  - **Severity**: Minor (but can impact usability)

- **Product Page - Filtering Options**
  - **Description**: The filtering options (A-Z, Z-A, low-high, high-low) do not function correctly for `problem_user`.
  - **Expected Behavior**: Changing filters should reflect visible changes to the product list.
  - **Actual Behavior**: Default listing is filtered A-Z, but changing filters results in no visible changes.

### Minor Issues
- **Product Page - Product Listings**
  - **Description**:
    - **For `standard_user`**:
      - Product Description Inconsistency: One product has a description that does not match the expected details.
      - Title Name Inconsistency: One product's title differs from the others, creating confusion.
    - **For `problem_user`**:
      - Image Display Issue: No images are appearing for the products listed.
  
- **User-Friendliness for Adding Items to Cart**
  - **Description**: 
    - For the `problem_user`, the "Remove" button is non-functional.
    - The quantity is not displayed after clicking "Add to Cart," leading to a lack of clarity on the number of items in the cart.

- **Reset App Status**
  - **Description**: Removes all items from the cart, but after this action, the "Add to Cart" button does not appear for selected items. Only the "Remove" button is displayed, leading to confusion about item availability.

---


