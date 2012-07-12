# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

import datetime

class ActivePriceManager(models.Manager):
    use_for_related_fields = True
    def get_query_set(self):
        return super(ActivePriceManager, self).get_query_set().filter(
            is_active=True,
            start_date__lte=datetime.date.today()
        )

class ActiveOrganizationDetailManager(models.Manager):
    use_for_related_fields = True
    def get_query_set(self):
        return super(ActiveOrganizationDetailManager, self).get_query_set().filter(
            is_active=True
        )

class ActiveClientDetailManager(models.Manager):
    use_for_related_fields = True
    def get_query_set(self):
        return super(ActiveClientDetailManager, self).get_query_set().filter(
            is_active=True
        )

class CreateOrderManager(models.Manager):
    use_for_related_fields = True
    def get_query_set(self):
        return super(CreateOrderManager, self).get_query_set().filter(
            state=settings.STATE_ORDER_CREATE
        )

class ReservOrderManager(models.Manager):
    use_for_related_fields = True
    def get_query_set(self):
        return super(ReservOrderManager, self).get_query_set().filter(
            state=settings.STATE_ORDER_RESERV
        )

class AcceptOrderManager(models.Manager):
    use_for_related_fields = True
    def get_query_set(self):
        return super(AcceptOrderManager, self).get_query_set().filter(
            state=settings.STATE_ORDER_ACCEPT
        )

class CloseOrderManager(models.Manager):
    use_for_related_fields = True
    def get_query_set(self):
        return super(CloseOrderManager, self).get_query_set().filter(
            state=settings.STATE_ORDER_CLOSE
        )

class CancelOrderManager(models.Manager):
    use_for_related_fields = True
    def get_query_set(self):
        return super(CancelOrderManager, self).get_query_set().filter(
            state=settings.STATE_ORDER_CANCEL
        )

class WorkOrderManager(models.Manager):
    use_for_related_fields = True
    def get_query_set(self):
        return super(WorkOrderManager, self).get_query_set().filter(
            state__in=settings.SELECT_WORK_ORDERS
        )

class CreateInvoiceManager(models.Manager):
    use_for_related_fields = True
    def get_query_set(self):
        return super(CreateInvoiceManager, self).get_query_set().filter(
            state=settings.STATE_INVOICE_CREATE
        )

class PaymentInvoiceManager(models.Manager):
    use_for_related_fields = True
    def get_query_set(self):
        return super(PaymentInvoiceManager, self).get_query_set().filter(
            state=settings.STATE_INVOICE_PAYMENT
        )

class CancelInvoiceManager(models.Manager):
    use_for_related_fields = True
    def get_query_set(self):
        return super(CancelInvoiceManager, self).get_query_set().filter(
            state=settings.STATE_INVOICE_CANCEL
        )

class SellerOrganizationManager(models.Manager):
    use_for_related_fields = True
    def get_query_set(self):
        return super(SellerOrganizationManager, self).get_query_set().filter(
            is_seller=True
        )

class BuyerOrganizationManager(models.Manager):
    use_for_related_fields = True
    def get_query_set(self):
        return super(BuyerOrganizationManager, self).get_query_set().filter(
            is_seller=False
        )

class PrivateClientManager(models.Manager):
    use_for_related_fields = True
    def get_query_set(self):
        return super(PrivateClientManager, self).get_query_set().filter(
            organization=None
        )
