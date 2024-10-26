# Exploratory Testing Report

**Project**: E-commerce Website  
**Tester**: Pramallika Chunduru  
**Date**: 26-10-2024  
**Version Control**: 

---

## 1. Test Charter
**Objective**: To evaluate the functionality and usability of the e-commerce website, focusing on core features such as login, product listings, cart functionality, and checkout processes.  
**Scope**: The testing concentrated on the login functionality, product page display, menu navigation, cart operations, and checkout process.

---

## 2. Environment
- **Browser and Version**: Chrome v93
- **Operating System**: Windows 10
- **Network Conditions**: Wi-Fi

---

## 3. Key Features Tested
### 1. Login Functionality
- Valid and invalid login attempts using different usernames.
- Error messages displayed for incorrect credentials.

### 2. Product Page
- Display of products including images, descriptions, and prices.
- Functionality of filtering options (A-Z, Z-A, low-high, high-low).

### 3. Menu Navigation
- Accessibility and functionality of menu options (All items, About, Logout, Reset App status).

### 4. Cart Functionality
- Adding and removing items from the cart.
- Quantity modification in the cart.

### 5. Checkout Process
- Input validation for first name, last name, and postcode during checkout.

---

## 4. Observations and Findings

### Summary of Observations and Findings

| Feature/Area Tested    | Observations                                                                          | Issues/Bugs                         |
|------------------------|---------------------------------------------------------------------------------------|-------------------------------------|
| Login Functionality    | Displays correct messages for login errors.                                           | - None found                        |
| Product Page           | Inconsistencies in product details for standard_user.                                 | - Issue #1, #2                      |
|                        | No pictures appear for products in some user types.                                   | - Issue #3                          |
|                        | Filters do not function properly for problem_user.                                    | - Issue #4                          |
| Menu Navigation        | About link is broken.                                                                 | - Issue #5                          |
|                        | Reset App status removes items, but buttons are inconsistent.                         | - Issue #6                          |
| Cart Functionality     | Unable to modify item quantity in the cart.                                           | - Issue #7                          |
|                        | Add to cart issues for problem_user: button disappears instead of showing quantity.   | - Issue #8                          |
| Checkout Process       | Accepts invalid formats for first name and last name fields.                          | - Issue #9                          |

---

## 5. Individual Issues

### Issue #1: Product Description Inconsistency
- **Description**: One product had an incorrect decscription (See Observation in Summary: Product Page)
- **Steps to Reproduce**:
  1. Log in as standard_user.
  2. Navigate to the product page.
  3. Identify the product with incorrect decscription.
- **Severity**: Minor

### Issue #2: Missing Product Images for Problem User
- **Description**: No images were displayed on the product list for the problem_user account. (See Observation in Summary: Product Page)
- **Severity**: Major

### Issue #3: Non-functional Filters for Problem User
- **Description**: Filtering options did not work; default listing remained unchanged regardless of filter selection. (See Observation in Summary: Product Page)
- **Severity**: Major

### Issue #4: Inconsistent Add to Cart Functionality
- **Description**: For some products, the add to cart button did not function properly, disappearing instead of showing the updated quantity. (See Observation in Summary: Cart Functionality)
- **Severity**: Critical

### Issue #5: Broken About Link
- **Description**: Clicking the "About" link led to a 404 error. (See Observation in Summary: Menu Navigation)
- **Severity**: Major

### Issue #6: Reset App Status Behavior
- **Description**: After resetting the app status, the add to cart button does not reappear on selected items. (See Observation in Summary: Menu Navigation)
- **Severity**: Minor

### Issue #7: Quantity Modification
- **Description**: Unable to change item quantity in the cart; default is set to 1. (See Observation in Summary: Cart Functionality)
- **Severity**: Critical

### Issue #8: Checkout Input Validation
- **Description**: The checkout process accepted invalid input formats (e.g., numbers for names). (See Observation in Summary: Checkout Process)
- **Severity**: Major

---

## 6. Ideas for Future Sessions
- Investigate how the application handles different user roles with special character inputs.
- Test the responsiveness of the website on various devices.
- Evaluate performance under different network conditions.

---

## 7. Suggestions for Improvements
- Implement better validation for checkout fields to prevent invalid inputs.
- Ensure filtering options work correctly for all user roles.
- Improve user interface consistency for adding/removing items from the cart.

---

## 8. Testing Session Duration
- **Duration**: 3 hours

---

## 9. Tools Used
- **Browser Developer Tools**: For inspecting elements and network activity.
- **Screenshot Tool**: For capturing issues.
- **Text Editor**: For documenting findings.

---
