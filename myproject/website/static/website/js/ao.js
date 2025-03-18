let currentPage = 1;
const productsPerPage = 12;
const totalProducts = 48; // Tổng số sản phẩm

function displayProducts(page) {
    const productList = document.getElementById('product-list');
    const start = (page - 1) * productsPerPage;
    const end = start + productsPerPage;
    const allProducts = Array.from(productList.children);

    allProducts.forEach((product, index) => {
        if (index >= start && index < end) {
            product.style.display = 'block';
        } else {
            product.style.display = 'none';
        }
    });
}

function changePage(page) {
    currentPage = page;
    displayProducts(currentPage);
}

function nextPage() {
    if (currentPage < totalProducts / productsPerPage) {
        currentPage++;
        displayProducts(currentPage);
    }
}

function prevPage() {
    if (currentPage > 1) {
        currentPage--;
        displayProducts(currentPage);
    }
}

// Khởi tạo lần đầu
displayProducts(currentPage);