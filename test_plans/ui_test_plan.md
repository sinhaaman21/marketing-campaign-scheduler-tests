# UI Test Plan for Marketing Campaign Scheduling Feature

## Test Cases

### 1. Campaign Creation Page
- **Test Case 1.1**: Verify the UI for creating a new email campaign.
  - **Steps**:
    1. Navigate to the campaign creation page.
    2. Enter campaign details (campaign name, send time and date).
    3. Save the campaign.
  - **Expected Result**: UI elements are functional, fields are easy to fill, and campaign is successfully created.

### 2. Recipient Selection Page
- **Test Case 2.1**: Verify the UI for selecting recipients.
  - **Steps**:
    1. Navigate to the recipient selection page.
    2. Choose a recipient list from the dropdown or search.
    3. Save the selection.
  - **Expected Result**: UI elements are functional, list is easy to navigate and select, and recipients are successfully saved.

### 3. Template Selection Page
- **Test Case 3.1**: Verify the UI for selecting email templates.
  - **Steps**:
    1. Navigate to the template selection page.
    2. Choose an email template from the list or search.
    3. Save the template.
  - **Expected Result**: UI elements are functional, templates are easy to view and select, and template is successfully saved.

### 4. Scheduled Campaigns Page
- **Test Case 4.1**: Verify the UI for viewing and editing scheduled campaigns.
  - **Steps**:
    1. Navigate to the scheduled campaigns page.
    2. Select a campaign.
    3. View campaign details.
  - **Expected Result**: UI elements are functional, campaign details are easy to view.
- **Test Case 4.2**: Verify the UI for editing details of a scheduled campaign.
  - **Steps**:
    1. Navigate to the scheduled campaigns page.
    2. Select a campaign.
    3. Edit campaign details (name, time, recipients, template).
    4. Save the changes.
  - **Expected Result**: UI elements are functional, fields are easy to edit, and changes are successfully saved.

### 5. Cancel Campaign Page
- **Test Case 5.1**: Verify the UI for canceling a campaign.
  - **Steps**:
    1. Navigate to the scheduled campaigns page.
    2. Select a campaign.
    3. Click the cancel button.
  - **Expected Result**: UI elements are functional, cancel process is clear, and campaign is successfully canceled.

## Device Compatibility Tests

### 6. Mobile Device Compatibility
- **Test Case 6.1**: Verify the UI on a mobile device.
  - **Steps**:
    1. Open the application on a mobile device or emulator.
    2. Execute Test Cases 1.1 to 5.1.
  - **Expected Result**: UI elements are functional and user-friendly on a mobile device.

### 7. Tablet Compatibility
- **Test Case 7.1**: Verify the UI on a tablet.
  - **Steps**:
    1. Open the application on a tablet or emulator.
    2. Execute Test Cases 1.1 to 5.1.
  - **Expected Result**: UI elements are functional and user-friendly on a tablet.

### 8. Cross-Browser Compatibility
- **Test Case 8.1**: Verify the UI across different browsers (Chrome, Firefox, Safari, Edge).
  - **Steps**:
    1. Open the application on each browser.
    2. Execute Test Cases 1.1 to 5.1.
  - **Expected Result**: UI elements are functional and consistent across different browsers.
