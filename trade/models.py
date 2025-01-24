from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import F

User = get_user_model()


# Create your models here.
class MasterItem(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    so_no = models.CharField(max_length=100, null=True, blank=True)
    po_no = models.CharField(max_length=100, null=True, blank=True)
    po_date = models.DateField(null=True, blank=True)
    bill_to = models.CharField(max_length=100, null=True, blank=True)
    customer_contact_details = models.CharField(max_length=100, null=True, blank=True)
    sales_engineer_name = models.CharField(max_length=100, null=True, blank=True)
    sales_office_name = models.CharField(max_length=100, null=True, blank=True)
    submitted_by = models.CharField(max_length=100, null=True, blank=True)
    submitted_date = models.DateField(null=True, blank=True)
    acknowledge_by = models.CharField(max_length=100, null=True, blank=True)
    acknowledge_date = models.DateField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    customer_name = models.CharField(max_length=100, null=True, blank=True)
    customer_number = models.CharField(max_length=100, null=True, blank=True)
    bill_to_gst = models.CharField(max_length=100, null=True, blank=True)
    ship_to_gst = models.CharField(max_length=100, null=True, blank=True)
    sold_to_gst = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class InlineItem(models.Model):
    items = models.ForeignKey(MasterItem, on_delete=models.CASCADE, related_name='inline_items')
    material_description = models.CharField(max_length=100, null=True, blank=True)
    material_no = models.CharField(max_length=100, null=True, blank=True)
    ms_code = models.CharField(max_length=100, null=True, blank=True)
    s_loc = models.CharField(max_length=100, null=True, blank=True)
    linkage_no = models.CharField(max_length=100, null=True, blank=True)
    item_status = models.CharField(max_length=100, null=True, blank=True)
    item_status_no = models.CharField(max_length=100, null=True, blank=True)
    imported_qty = models.IntegerField(null=True, blank=True)
    exported_qty = models.IntegerField(null=True, blank=True)
    revision_flag = models.BooleanField(default=False)
    revision_count = models.IntegerField(null=True, blank=True)
    unit_of_measurement = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    status_no = models.CharField(max_length=100, null=True, blank=True)
    item_no = models.CharField(max_length=100, null=True, blank=True)
    warranty_date = models.DateField(null=True, blank=True)
    warranty_flag = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text='Only USD amount', null=True, blank=True)
    total_amount = models.GeneratedField(expression=F('price') - F('quantity'), output_field=models.BigIntegerField(),db_persist=True)
    is_active = models.BooleanField(default=True)


class ImportBatch(models.Model):
    item = models.ForeignKey(MasterItem, on_delete=models.CASCADE, related_name='batches')
    quantity = models.PositiveIntegerField()
    import_date = models.DateField()
    batch_number = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Batch {self.batch_number} - {self.item.name}'


class BillingDetail(models.Model):
    import_batch = models.ForeignKey(ImportBatch, on_delete=models.CASCADE, related_name='billing_details')
    billing_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Billing for {self.import_batch} on {self.billing_date}'


# Create for Item Approval
class UserRequestAllocation(models.Model):
    emp_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    item_id = models.ForeignKey(MasterItem, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, null=True, blank=True)
    approve_status = models.CharField(max_length=200, default="Approver")
    approver_flag = models.BooleanField(default=False)
    approved_date = models.DateTimeField(auto_now_add=True, null=True)
    remarks = models.CharField(max_length=500, null=True, blank=True)
    approver_stage = models.CharField(max_length=200, null=True, blank=True)
    approver_level = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)


class AuthThreads(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    item_id = models.ForeignKey(MasterItem, null=True, on_delete=models.CASCADE)
    emp_id = models.IntegerField(null=True)
    remarks = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    approver = models.CharField(max_length=50, null=True, blank=True)
    assign_list = models.CharField(max_length=250, null=True, blank=True)
    is_active = models.BooleanField(default=True)
