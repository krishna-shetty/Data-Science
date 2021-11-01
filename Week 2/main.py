from imbox import Imbox
import mysql.connector


with Imbox('imap.gmail.com',
        username = 'krishnaharishshetty@gmail.com',
        password = '-----',
        ssl=True,
        ssl_context=None,
        starttls=False) as imbox:
        inbox = imbox.messages(sent_from = 'krishna.shetty@somaiya.edu')

        for uid,message in inbox:
            message.sent_from
            message.sent_to
            message.subject
            message.headers
            message.message_id
            message.date
            message.body
            message.attachments
            body = message.body

            text = str(body['plain'][0])
            final = text.split()
            invoice_num = str(final[6])
            invoice_date = final[3]
            product_list = []
            products = " "
            for i in final[9:]:
                if(i == 'Billing'):
                    break
                product_list.append(i)
            for temp in product_list:
                products = products + temp + " "
            for i in range(len(product_list) - 1):
                product_list[i] = product_list[i].replace(',', '')
            address = []
            billing_address = " "
            for i in final[11 + len(product_list):]:
                if(i == '--'):
                    break
                address.append(i)
            for temp in address:
                billing_address  = billing_address + temp + " "
            client_name = final[0]

connection = mysql.connector.connect(host = 'localhost', database = 'invoicing', user = 'root', password = '-----')
cursor = connection.cursor()
cursor.callproc('insert_invoice', (invoice_num, client_name, invoice_date, billing_address))
for x in product_list:
    cursor.callproc('insert_products_into_invoiceitems', (x, invoice_num))
connection.commit()
cursor.close() 
connection.close()
