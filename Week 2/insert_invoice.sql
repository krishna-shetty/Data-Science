CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_invoice`(num VARCHAR(15), clientname VARCHAR(50), invoicedate VARCHAR(45), billingaddress VARCHAR(100))
BEGIN
	INSERT INTO invoices (number, client_id, invoice_date, billing_address)
    VALUES (num, 
			(SELECT client_id
            FROM clients 
            WHERE name = clientname),
            invoicedate,
            billingaddress);
END