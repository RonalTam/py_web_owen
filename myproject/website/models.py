from django.db import models

# Create your models here.
class SanPham(models.Model):
    ten = models.CharField(max_length=100)  # name
    duong_dan = models.SlugField(unique=True)  # slug
    mo_ta = models.TextField(blank=True)  # description
    gia = models.DecimalField(max_digits=12, decimal_places=0)  # price
    hinh_anh = models.ImageField(upload_to='san_pham/')  # image
    ngay_tao = models.DateTimeField(auto_now_add=True)  # created_at

    def __str__(self):
        return self.ten