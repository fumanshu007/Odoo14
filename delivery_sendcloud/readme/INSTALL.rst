In the Odoo configuration file add ``delivery_sendcloud`` in the list
``server_wide_modules``:

.. code-block:: ini

  [options]
  (...)
  server_wide_modules = web,delivery_sendcloud
  (...)

A restart of the Odoo server is required afterwards.