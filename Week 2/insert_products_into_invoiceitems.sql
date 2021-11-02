CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_products_into_invoiceitems`(productname VARCHAR(15), invoicenumber VARCHAR(15))
BEGIN
	INSERT INTO invoice_items
    VALUES ((SELECT invoice_id
			FROM invoices
            WHERE number = invoicenumber),
			(SELECT product_id
			FROM products
            WHERE name = productname));
END