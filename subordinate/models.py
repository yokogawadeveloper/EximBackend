from django.db import models


class AdvanceAuthorization(models.Model):
    authorization_number = models.CharField(max_length=15, unique=True)
    authorization_date = models.DateField()
    import_validity_date = models.DateField()
    export_validity_date = models.DateField()
    foreign_currency = models.CharField(max_length=5)  # Currency symbol
    fob_value_inr = models.DecimalField(max_digits=12, decimal_places=2)
    fob_value_foreign = models.DecimalField(max_digits=12, decimal_places=2)
    cif_value_inr = models.DecimalField(max_digits=12, decimal_places=2)
    cif_value_foreign = models.DecimalField(max_digits=12, decimal_places=2)
    port_of_registration = models.CharField(max_length=30)
    customs_notification_no = models.CharField(max_length=15, null=True, blank=True)
    customs_notification_date = models.DateField(null=True, blank=True)
    payment_confirmation_received = models.BooleanField(default=False)
    ebrc_date = models.DateField(null=True, blank=True)
    eodc_application_date = models.DateField(null=True, blank=True)
    bond_cancellation_date = models.DateField(null=True, blank=True)
    authorization_status = models.CharField(max_length=25)
    authorization_status_remarks = models.CharField(max_length=100, blank=True)
    project_manager = models.CharField(max_length=20)
    bu_name = models.CharField(max_length=10)


# Import Master
class ImportMaster(models.Model):
    advance_authorization = models.ForeignKey(AdvanceAuthorization, on_delete=models.CASCADE,
                                              related_name='import_records')
    input_description = models.CharField(max_length=50)
    technical_feature_description = models.CharField(max_length=150)
    itchs_code = models.CharField(max_length=8)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    uom = models.CharField(max_length=10)
    cif_value_inr = models.DecimalField(max_digits=12, decimal_places=2)
    cif_value_foreign = models.DecimalField(max_digits=12, decimal_places=2)


class ActualImportTransaction(models.Model):
    import_master = models.ForeignKey(ImportMaster, on_delete=models.CASCADE, related_name='actual_import_transactions')
    bill_of_entry_no = models.CharField(max_length=7)
    bill_of_entry_date = models.DateField()
    igm_no = models.CharField(max_length=10, null=True, blank=True)
    igm_date = models.DateField(null=True, blank=True)
    awb_no = models.CharField(max_length=20, null=True, blank=True)
    awb_date = models.DateField(null=True, blank=True)
    supplier_name = models.CharField(max_length=50)
    port_of_loading = models.CharField(max_length=20)
    import_invoice_no = models.CharField(max_length=20)
    import_invoice_date = models.DateField()
    qty_imported = models.DecimalField(max_digits=10, decimal_places=2)
    cif_value_imported = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Import Transaction {self.bill_of_entry_no} for {self.import_master}"


# Export Master
class ExportMaster(models.Model):
    advance_authorization = models.ForeignKey(AdvanceAuthorization, on_delete=models.CASCADE,
                                              related_name='export_records')
    item_to_be_exported = models.CharField(max_length=50)
    item_characteristics = models.CharField(max_length=150)
    itchs_code = models.CharField(max_length=8)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    uom = models.CharField(max_length=10)
    fob_value_inr = models.DecimalField(max_digits=12, decimal_places=2)
    fob_value_foreign = models.DecimalField(max_digits=12, decimal_places=2)


class ActualExportTransaction(models.Model):
    export_master = models.ForeignKey(ExportMaster, on_delete=models.CASCADE, related_name='actual_export_transactions')
    shipping_bill_no = models.CharField(max_length=7)
    shipping_bill_date = models.DateField()
    marks_and_numbers = models.CharField(max_length=200, null=True, blank=True)
    container_details = models.CharField(max_length=200, null=True, blank=True)
    bl_awb_no = models.CharField(max_length=20, null=True, blank=True)
    bl_awb_date = models.DateField(null=True, blank=True)
    customer_name = models.CharField(max_length=50)
    port_of_discharge = models.CharField(max_length=20)
    export_invoice_no = models.CharField(max_length=20)
    export_invoice_date = models.DateField()
    qty_exported = models.DecimalField(max_digits=10, decimal_places=2)
    fob_value_exported_inr = models.DecimalField(max_digits=12, decimal_places=2)
    fob_value_exported_foreign = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Export Transaction {self.shipping_bill_no} for {self.export_master}"


# Payment details related to Export Master
class PaymentDetails(models.Model):
    shipping_bill_no = models.CharField(max_length=7)
    bank_name = models.CharField(max_length=25)
    bill_id_no = models.CharField(max_length=20)
    bank_realisation_certificate_no = models.CharField(max_length=40)
    date_of_realisation = models.DateField()
    realised_value_foreign_currency = models.DecimalField(max_digits=12, decimal_places=2)
