Odoo Integration
~~~~~~~~~~~~~~~~

Verify that the value of "web.base.url" parameter in System Parameters is set with
the correct url (eg.: "https://demo.onestein.eu" instead of "http://localhost:8069").

- Go to SendCloud > Configuration > Wizards > Setup the SendCloud Integration. A wizard will pop up.
- Confirm. You will be redirected to a SendCloud page asking you to authorize OdooShop to access your Sendcloud account.
- Click on Connect in the SendCloud page.
- Go back to the Odoo Integration configuration. An integration "OdooShop" is now present in the Integration list view. Open the OdooShop Integration form.
- Edit the OdooShop Integration. The changes you make will be in sync, SendCloud side, with the integration configuration.

In case multiple integrations are present, sort the integrations by sequence, to allow
Odoo to choose the default one that will be used.

API Integration
~~~~~~~~~~~~~~~

Go to SendCloud > Configuration > Wizards > Setup the SendCloud Integration. Click on Setup Integration. A wizard will pop up.

Select API Integration. Confirm.
Enter the public and secret keys provided by SendCloud.
Here is how to create api key in SendCloud:
https://github.com/SendCloud/api-integration-example

Confirm. An API integration is now present in the Integration list view.
Open the API Integration form.
Edit the API Integration. The changes you make will be in sync, SendCloud side, with the integration configuration.


SendCloud panel settings
~~~~~~~~~~~~~~~~~~~~~~~~

When you configure the Integration settings in the online SendCloud panel (https://panel.sendcloud.sc/)
those settings are also sync-ed with the Integration settings Odoo side.


Synchronize SendCloud objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After the setup of the integration with SendCloud server is completed, second step is
to synchronize the objects present in SendCloud server to Odoo.
To synchronize SendCloud objects for the first time:

- Go to SendCloud > Configuration > Wizards > Sync the SendCloud Objects. A wizard will pop up.
- Select all the objects. Confirm. This will retrieve the required data from SendCloud server.

Some SendCloud objects will be automatically synchronized from the SendCloud server to Odoo.
Those SendCloud objects are:

- Parcel Statuses
- Invoices
- Shipping Methods
- Sender Addresses

To configure how often those objects should be retrieved from the SendCloud server:

- Go to Settings > Technical > Automation > Scheduled Actions. Search Scheduled Actions for "SendCloud".
- Set the "Execute Every" value according to your needs.


Sender Addresses and Warehouses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In case of multiple warehouses configured in Odoo (eg.: user belongs to group "Manage multiple Warehouse"):

Go to SendCloud > Configuration > Wizards > Setup the sender addresses of the warehouses. A wizard will pop up.
Set the corresponding Sendcloud Sender Address for each of the warehouse addresses.

Alternatively, in Inventory > Configuration > Warehouses, select an address. In the address form, go to Sales and Purchase tab and set the Sencloud Sender Address.
In Sale Order > Delivery: select the Warehouse. Check that the address of the Warehouse has a Sendcloud Senser Address.

Initial sync of past orders
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once all the previous configuration steps are completed, it is possible to synchronize
all the past Odoo outgoing shipments to Sendcloud.
Those shipments are the ones already setup with a SendCloud shipping method.

Go to SendCloud > Configuration > Wizards > Sync past orders to SendCloud. A wizard will pop up.
Select the date (by default set to 30 days back from today) from which the shipments
must be synchronized.

Click on Confirm button: the shipments will be displayed in the Incoming Order View tab of the Sendcloud panel.
They will contain a status “Ready to Process” if they are ready to generate a label and the order fulfillment will continue.

Test Mode
~~~~~~~~~

To enable the Test Mode, go to the "General Settings": under the SendCloud section you can find the "Enable Test Mode" flag.
Enabling the Test Mode allows you to access extra functionalities that are useful to test the connector.
