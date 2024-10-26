# Exploratory Testing Report

**Project**: Technical_Assessment_TestEng  
**Tester**: Pramallika Chunduru  
**Date**: 26-10-2024 
**Version Control**: https://github.com/Pramallika/Technical_Assessment_TestEng.git

---

## 1. Test Charter
**Objective**:To evaluate the functionality and usability of the e-commerce website, focusing on core features and identifying any unexpected behaviors during interaction.  
**Scope**: This exploratory test focused on the login process, product listing, shopping cart functionality, and menu navigation.

---

## 2. Environment
- **Browser and Version**: Chrome v93
- **Operating System**: Windows 10
- **Network Conditions**: Wi-Fi

---

## 3. Observations

### Summary of Observations and Findings
| Feature/Area Tested    | Observations                               | Issues/Bugs |
|------------------------|--------------------------------------------|-------------|
| **Login Functionality**| The login process worked smoothly for valid credentials. Error messages displayed correctly for invalid logins. However, performance_glitch_user experienced slower loading times. Additionally, after an incorrect password entry, the show password icon disappears until the password field is cleared. | - |
| **Product Page**       | Product listings were generally clear, showing images, descriptions, and prices. However, there were inconsistencies in product descriptions and titles for one product when logged in as standard_user. For problem_user, product images did not display, and filtering options were unresponsive. | Inconsistencies in product info (Issue #1),(Issue #2), Filter issues (Issue #3) |
| **Shopping Cart**      | The "Add to Cart" button functioned correctly for standard_user but encountered issues for problem_user, where the button is not clickable and does not add the item. Quantity adjustments were not possible on the cart page, and incorrect formats (e.g., numbers for names) were accepted during checkout. | Add to Cart issue (Issue #4), Checkout validation issue (Issue #5) |
| **Menu Navigation**    | All menu options performed well, but the "About" link was broken. The "Reset App Status" function cleared the cart but did not restore the "Add to Cart" button for selected items. Performance_glitch_user experienced slow load times across all pages. | Broken About link (Issue #6), Reset function issue (Issue #7) |

### Individual Issues
#### Issue #1: Inconsistency in Product Description
- **Description**: For standard_user, one product's description did not match the expected format.
- **Expected Result**: Consistent product information.
- **Actual Result**: Discrepancy in the displayed data.
- **Severity**: Minor

  #### Issue #2: Inconsistency in Product title
- **Description**: For standard_user, one product's title did not match the expected format.
- **Expected Result**: Consistent product information.
- **Actual Result**: Discrepancy in the displayed data.
- **Severity**: Minor

#### Issue #3: Non-Functional Filters for Problem User
- **Description**: The filtering options did not work as intended; default listings remained unchanged despite user input.
- **Expected Result**: Filters should apply immediately to the product listings.
- **Actual Result**: No change in product display.
- **Severity**: Major

#### Issue #4: Add to Cart Button is not clickable for Problem User
- **Description**: When the "Add to Cart" button was clicked for certain products, it was not clickable, and the item was not added to the cart.
- **Expected Result**: Item should be added, and quantity should update.
- **Actual Result**: Button does not work with no confirmation of the action.
- **Severity**: Major

#### Issue #5: Checkout Accepting Incorrect Formats
- **Description**: The checkout process allowed invalid inputs (numbers for first name and last name).
- **Expected Result**: The form should validate input types.
- **Actual Result**: Incorrect formats accepted without error.
- **Severity**: Critical

#### Issue #6: Broken About Link
- **Description**: The "About" page link led to a 404 error.
- **Severity**: Major

#### Issue #7: Reset Functionality Inconsistency
- **Description**: Resetting the app cleared items from the cart but did not restore the "Add to Cart" button functionality for products.
- **Severity**: Minor

---

## 4. Ideas for Future Sessions
- Investigate the error handling for invalid input data more thoroughly.
- Explore the usability of the website on mobile devices to test responsiveness.
- Perform stress testing by logging in with multiple user accounts simultaneously to evaluate performance under load.

## 5. Suggestions for Improvements
- Improve the validation checks during the checkout process to prevent incorrect data submissions.
- Ensure product descriptions and titles are consistent and accurate across all user types.
- Fix the filtering functionality to ensure that users can sort products as expected.

---

## Conclusion
This exploratory testing session revealed several critical issues that need to be addressed to enhance the overall user experience. Addressing these findings will improve the functionality and reliability of the website.
