CREATE SCHEMA "ecom";
ALTER SCHEMA "ecom" CHANGE OWNER SYS;


CREATE TABLE "ecom"."DATEDM" (
		"ID" DECIMAL(18,0) IDENTITY NOT NULL ,
		"PURCHASE_DATE" TIMESTAMP ,
		"APPROVED_DATE" TIMESTAMP ,
		"DELIVERED_CARRIER_DATE" TIMESTAMP ,
		"DELIVERED_CUSTOMER_DATE" TIMESTAMP ,
		"ESTIMATE_DELIVERY_DATE" TIMESTAMP ,
		"SHIPPING_LIMIT_DATE" TIMESTAMP
);
;

ALTER TABLE "ecom".DATEDM ADD CONSTRAINT DATEDM_PK PRIMARY KEY ("ID")  ENABLE ;

CREATE TABLE "ecom"."PAYMENTS" (
		"ID" DECIMAL(18,0) IDENTITY NOT NULL ,
		"PAYMENT_TYPE" VARCHAR(50) UTF8 ,
		"INSTALLMENTS" DECIMAL(18,0) ,
		"PAYMENT_VALUE" DOUBLE
);
;

ALTER TABLE "ecom".PAYMENTS ADD CONSTRAINT PAYMENTS_PK PRIMARY KEY ("ID")  ENABLE ;

CREATE TABLE "ecom"."PRODUCT" (
		"ID" DECIMAL(18,0) IDENTITY NOT NULL ,
		"IDD" VARCHAR(50) UTF8 ,
		"CATEGORY" VARCHAR(255) UTF8 ,
		"PRICE" DOUBLE ,
		"FREIGHT_VALUE" DOUBLE
);
;

ALTER TABLE "ecom".PRODUCT ADD CONSTRAINT PRODUCT_PK PRIMARY KEY ("ID")  ENABLE ;

CREATE TABLE "ecom"."USER" (
		"ID" DECIMAL(18,0) IDENTITY NOT NULL ,
		"IDD" VARCHAR(50) UTF8 ,
		"ZIPCODE" VARCHAR(50) UTF8 ,
		"CITY" VARCHAR(50) UTF8 ,
		"USER_STATE" VARCHAR(50) UTF8
);
;

ALTER TABLE "ecom"."USER" ADD CONSTRAINT USER_PK PRIMARY KEY ("ID")  ENABLE ;

CREATE TABLE "ecom"."ORDERS" (
		"ID" DECIMAL(18,0) IDENTITY NOT NULL ,
		"ORDER_ID" VARCHAR(50) UTF8 ,
		"CUSTOMER_ID" DECIMAL(18,0) ,
		"PAYMENT_ID" DECIMAL(18,0) ,
		"SELLER_ID" DECIMAL(18,0) ,
		"PRODUCT_ID" DECIMAL(18,0) ,
		"STATUS" VARCHAR(50) UTF8 ,
		"ITEMS" DECIMAL(18,0) ,
		"DATE_ID" DECIMAL(18,0)
);
;

ALTER TABLE "ecom".ORDERS ADD CONSTRAINT ORDERS_PK PRIMARY KEY ("ID")  ENABLE ;

ALTER TABLE "ecom".ORDERS ADD CONSTRAINT CUSTOMER_FK FOREIGN KEY (CUSTOMER_ID) REFERENCES "ecom"."USER" (ID) ENABLE ;

ALTER TABLE "ecom".ORDERS ADD CONSTRAINT DATE_FK FOREIGN KEY (DATE_ID) REFERENCES "ecom".DATEDM (ID) ENABLE ;

ALTER TABLE "ecom".ORDERS ADD CONSTRAINT PAYMENT_FK FOREIGN KEY (PAYMENT_ID) REFERENCES "ecom".PAYMENTS (ID) ENABLE ;

ALTER TABLE "ecom".ORDERS ADD CONSTRAINT PRODUCT_FK FOREIGN KEY (PRODUCT_ID) REFERENCES "ecom".PRODUCT (ID) ENABLE ;

ALTER TABLE "ecom".ORDERS ADD CONSTRAINT SELLER_FK FOREIGN KEY (SELLER_ID) REFERENCES "ecom"."USER" (ID) ENABLE ;
