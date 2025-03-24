from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import SanPham


# Create your views here.
def home(request):
    danh_sach_san_pham = SanPham.objects.all()

    return render(
        request, "website/home.html", {"danh_sach_san_pham": danh_sach_san_pham}
    )


def ao_view(request):
    return render(request, "website/ao.html")


def chi_tiet_san_pham(request, product_id):
    san_pham = get_object_or_404(SanPham, pk=product_id)
    sizes = ["S", "M", "L", "XL", "2XL"]
    return render(
        request, "website/chi_tiet_san_pham.html", {"sp": san_pham, "sizes": sizes}
    )


def them_vao_gio_hang(request, product_id):
    sp = get_object_or_404(SanPham, pk=product_id)
    size = request.POST.get("size")
    if not size:
        return redirect("chi_tiet_san_pham", product_id=product_id)

    gio = request.session.get("gio", [])
    check = False
    for item in gio:
        if item["id"] == sp.id and item["size"] == size:
            item["so_luong"] += 1
            check = True
            break

    # Thêm vào giỏ hàng
    if not check:
        gio.append(
            {
                "id": sp.id,
                "ten": sp.ten,
                "gia": int(sp.gia),
                "hinh_anh": sp.hinh_anh.url,
                "size": size,
                "so_luong": 1,
            }
        )

    request.session["gio"] = gio
    request.session.modified = True
    messages.success(request, "Đã thêm vào giỏ hàng thành công!")
    return redirect("chi_tiet_san_pham", product_id=product_id)


def gio_hang(request):
    gio = request.session.get("gio", [])
    tong_so_luong = sum(item["so_luong"] for item in gio)
    tong_tien = sum(item["so_luong"] * item["gia"] for item in gio)

    return render(
        request,
        "website/cart.html",
        {"gio": gio, "tong_so_luong": tong_so_luong, "tong_tien": tong_tien},
    )


def xoa_san_pham(request):
    if request.method == "POST":
        product_id = int(request.POST.get("id"))
        size = request.POST.get("size")
        gio = request.session.get("gio", [])

        # Xóa đúng sản phẩm theo ID và Size bằng cách loại sản phẩm có id và size được chọn ra khỏi giogio
        gio = [
            item
            for item in gio
            if not (item["id"] == product_id and item["size"] == size)
        ]

        request.session["gio"] = gio
        request.session.modified = True
    return redirect("gio_hang")

def checkout(request):
    gio = request.session.get('gio', [])
    if not gio:
        messages.warning(request, 'Giỏ hàng đang trống!')
        return redirect('gio_hang')

    if request.method == 'POST':
        ho_ten = request.POST.get('ho_ten')
        dien_thoai = request.POST.get('dien_thoai')
        dia_chi = request.POST.get('dia_chi')

        # Xóa giỏ hàng sau khi đặt
        request.session['gio'] = []
        return redirect('home')
    tong_so_luong = sum(item["so_luong"] for item in gio)
    tong_tien = sum((item["so_luong"] * item["gia"]) for item in gio)
    thanh_tien = sum((item["so_luong"] * item["gia"]) + 30000 for item in gio)
    return render(request, 'website/checkout.html', {'gio': gio, "tong_tien": tong_tien, "tong_so_luong": tong_so_luong, "thanh_tien": thanh_tien})