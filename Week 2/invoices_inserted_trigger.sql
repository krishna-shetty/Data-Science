USE  'invoicing'
DELIMITER $$
CREATE TRIGGER invoices_inserted_trigger
AFTER INSERT ON invoices 
FOR EACH ROW
BEGIN
INSERT INTO audit_log (event_type)
	VALUES('New record inserted into invoices table');
END$$