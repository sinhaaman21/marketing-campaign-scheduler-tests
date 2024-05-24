# Integration Test Plan for Marketing Campaign Scheduling Feature

## Services and Integration Points

### 1. Integration with Recipient Management Service
- **Test Case 1.1**: Verify integration with the recipient management service.
  - **Steps**:
    1. Create a campaign.
    2. Select a recipient list.
  - **Expected Result**: Recipient list is retrieved and saved for the campaign.

### 2. Integration with Email Template Service
- **Test Case 2.1**: Verify integration with the email template service.
  - **Steps**:
    1. Create a campaign.
    2. Select an email template.
  - **Expected Result**: Email template is retrieved and saved for the campaign.

### 3. Scheduling and Sending Emails
- **Test Case 3.1**: Verify scheduling and sending emails via the external email service.
  - **Steps**:
    1. Schedule a campaign.
    2. Verify the campaign is sent at the specified time.
  - **Expected Result**: Emails are sent to recipients at the scheduled time.
