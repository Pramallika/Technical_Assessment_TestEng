# Test Plan for Functional Testing

### Author: Pramallika Chunduru
### Date: 30-10-2024

---

## 1. Objective

The purpose of this test plan is to validate the core functionalities of (https://www.saucedemo.com/v1/index.html) website, ensuring that key user flows, input validations, and session management perform as expected. The aim is to create a seamless, reliable shopping experience by focusing on areas critical to the user journey, including login, product interactions, cart management, and checkout processes.

---

## 2. Scope of Testing

The testing scope includes both **manual** and **automated** testing to ensure comprehensive coverage of core functionalities:

### Manual Testing
- **Login Flow**: Verifying successful login and error handling for each user type to capture edge cases that may not be suitable for automation.
- **Checkout Process**: Manually testing the checkout process ensures thorough verification of user experience and handling of complex scenarios like discounts or promotions.
- **Error Messaging**: Manually checking error messages for clarity and usability, as these often require subjective assessment of the user interface.
  
> *Manual testing is chosen for areas that require subjective assessment or involve complex, less-repeatable scenarios, while automation is focused on repeatable, critical flows where efficiency and consistency add high value.*

### Automated Testing
The following areas will be automated to optimize testing resources, enhance efficiency, and ensure repeatability:

- **Login Flow**: Automating successful login and error scenarios allows for quick regression checks with each build, ensuring that authentication processes are robust.
- **Product and Cart Management**: Automating product interactions (add/remove items) and cart updates is critical as these actions are frequently performed by users and need to be verified continuously.
- **Checkout Process**: Automating input validation and the end-to-end checkout flow provides consistent testing of essential user journeys, minimizing human error and ensuring accuracy in data handling.
- **Sorting Products**: Automating the sorting functionality for product listings is essential to ensure that users can easily find and select items based on various criteria. This involves validating that the sorting algorithm works correctly across all categories and that the results are consistent and accurate. Regularly testing this feature can help catch any discrepancies in product ordering that may arise due to changes in the backend or database updates. Additionally, it ensures that any new sorting options introduced are functional and do not interfere with existing capabilities.

This approach balances manual testing's depth and automation's efficiency, ensuring that the most critical paths are thoroughly validated without overburdening resources.

---

### Out-of-Scope Functionalities
This test plan does not include:
- Back-end database validation.
- Payment gateway integration testing.
- Extensive performance testing for load and stress scenarios.

---

## 3. Test Approach

### Rationale for the Test Approach
This approach is selected to balance **functional coverage** and **efficiency** by prioritizing the critical paths and input validations that users frequently encounter. By focusing on end-to-end user flows, input boundaries, and key functional components, we can cover scenarios that represent real-world usage while efficiently detecting potential issues in high-risk areas. This ensures that the essential functions work as expected under various conditions and that the application can handle both typical and edge-case inputs.

### Testing Types and Prioritized Functional Tests
The following are prioritized based on their impact on the primary user experience:

1. **Input Validation**: Test each form and field for correct behavior with valid and invalid data (e.g., required fields in the checkout, email format validation).
2. **Boundary Testing**: Ensure fields and numeric inputs honor maximum and minimum values (e.g., max quantity in cart).
3. **User Flow Tests**: End-to-end scenarios from login to checkout, covering product interactions, cart operations, and checkout.
4. **Session Management**: Verifying session persistence and logout behavior, ensuring a consistent experience throughout.
5. **Navigation and Redirects**: Confirming that all main links redirect users appropriately and reliably.
6. **Cart Management**: Verifying that cart contents and subtotals update correctly with each add/remove action.
7. **Error Messaging**: Checking that error messages are clear, accurate, and triggered when expected.
8. **Cross-Browser Testing**: Testing on Chrome, Firefox, Safari, and Edge to ensure consistency.
9. **Basic Performance Checks**: Verifying load times for product pages, cart, and checkout.

---

## 4. Tools and Frameworks

### Test Management and Documentation
- **GitHub**: For documentation, test case tracking, and issue reporting.
- **Markdown Files**: To document test cases, test results, and defect tracking.

### Automation Tool and Framework Justification
- **Selenium with Python**: Selenium is a powerful tool for web application testing, providing cross-browser support and robust interaction with web elements. Python is chosen for its readability, extensive library support, and compatibility with Selenium. Together, Selenium and Python will allow us to efficiently automate repetitive and critical flows in the user journey, such as login, product interactions, and checkout. This combination is ideal for automating the e-commerce workflows, ensuring consistency across multiple test runs and quick detection of regressions.
  

### Additional Libraries
- **unittest**: Utilized for structured and modular test case organization, enabling developers to create and manage test suites effectively. This framework provides built-in assertions and facilitates test discovery, allowing for comprehensive reporting on test results and simplifying the debugging process.
- **Selenium WebDriver**: For direct control over the browser, supporting cross-browser tests.

### Test Data Management Strategy
- **Reusable Test Data**: Establish reusable accounts and static test data for users and products to maintain consistency across tests, while dynamically generating unique order or cart entries as needed.


---

## 5. Test Execution Plan

### Prioritized Functional Test Cases

#### A. Input Validation
| Test Case | Description |
|-----------------------------------|---------------------------------------------------------------------------------------------------|
| **Checkout Form Validation** | Verify required fields (name, address) display error messages if left empty. |
| **Field Format Checks** | Ensure incorrect formats (e.g., numbers in name fields, special characters) trigger validation. |

#### B. Boundary Testing
| Test Case | Description |
|-----------------------------------|---------------------------------------------------------------------------------------------------|
| **Cart Quantity Limits** | Test min/max allowable quantities in the cart to ensure limits are enforced. |
| **Character Limit on Fields** | Verify character limits in fields like name and address to prevent overflow or truncation issues. |

#### C. User Flow Tests
| Test Case | Description |
|-----------------------------------|---------------------------------------------------------------------------------------------------|
| **Login Flow** | Test login success and failure scenarios for each user type. |
| **Product to Checkout Flow** | End-to-end test from login through adding items to cart and completing checkout. |
| **Cart Update and Navigation** | Verify items can be added/removed and cart updates accurately between pages. |

#### D. Session Management
| Test Case | Description |
|-----------------------------------|---------------------------------------------------------------------------------------------------|
| **Session Persistence** | Ensure users remain logged in during the session and cart contents persist. |
| **Logout Functionality** | Verify that logout removes session data and redirects to login. |

#### E. Navigation and Redirects
| Test Case | Description |
|-----------------------------------|---------------------------------------------------------------------------------------------------|
| **Menu Links (About, Logout)** | Test each menu item redirects to the correct page and maintains session as appropriate. |
| **Continue Shopping Button** | Verify that “Continue Shopping” returns users to the product page from the cart. |

#### F. Cart Management
| Test Case | Description |
|-----------------------------------|---------------------------------------------------------------------------------------------------|
| **Add/Remove Items** | Confirm items can be added and removed correctly, and the subtotal updates accurately. |
| **Empty Cart Behavior** | Test emptying the cart to ensure no errors when proceeding to checkout with an empty cart. |

#### G. Error Messaging
| Test Case | Description |
|-----------------------------------|---------------------------------------------------------------------------------------------------|
| **Login Error Messages** | Verify that incorrect logins display the appropriate error message. |
| **Form Validation Errors** | Check that missing or incorrect inputs on the checkout form trigger the correct error messages. |

#### H. Cross-Browser Testing
| Test Case                   | Description                                                                                   |
|-----------------------------|-----------------------------------------------------------------------------------------------|
| **Multi-Browser Compatibility** | Test main workflows on Chrome, Firefox, Safari, and Edge to verify UI and functionality consistency. |

--- 



### Timeline and Milestones

| Activity            | Estimated Time | Priority |
|---------------------|----------------|----------|
| Exploratory Testing | 1 hour         | High     |
| Functional Testing  | 4 hours        | High     |
| Edge Case Testing   | 2 hours        | Medium   |
| Automation Scripting |               |          |
| - Login Flow        | 1 hour         | High     |
| - Product and Cart  | 1.5 hours      | High     |
| - Checkout Process  | 1.5 hours      | High     |
| - Sort Products Tests  | 1 hour         | Medium   |

---

## 6. Defect Tracking and Reporting

Defects will be logged in Bugs.md file, categorized by priority:
- **Critical**: Blocks main flows, such as login or checkout errors.
- **Major**: Impacts usability, like incorrect cart updates.
- **Minor**: Minor visual or text issues, such as label formatting.

---

### Risk Analysis

| Risk | Mitigation Strategy |
|------------------------------------|--------------------------------------------------------------|
| **Automation Test Flakiness** | Use explicit waits to handle dynamic elements consistently. Use modularized automation scripts to isolate dynamic element handling and enhance maintainability of tests as the application evolves. |
| **Time Constraints** | Prioritize core user flows first to ensure coverage. |
| **Browser Compatibility** | Execute automation tests across multiple browsers. |
---

## 8. Conclusion

This test plan is designed to validate critical functional areas of the e-commerce website, emphasizing a seamless user journey through core flows like login, product interactions, cart, and checkout. By targeting high-impact user interactions, input validation, session management, and cross-browser consistency, this approach aims to deliver a reliable and intuitive shopping experience.

Using Selenium with Python for automation will expedite the testing of repetitive flows and reduce the time required for regression tests, enabling faster identification and resolution of defects. Comprehensive risk mitigation strategies, structured timelines, and efficient test data management support delivering a high-quality product aligned with user expectations.

---



