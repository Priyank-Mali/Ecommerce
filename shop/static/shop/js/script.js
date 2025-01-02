

function clearCart(){
    cart = JSON.parse(localStorage.getItem("cart"))
    for (let item in cart){
        document.getElementById(`div${item}`).innerHTML = `
        <button id="pr{{product.product_id}}" class="btn btn-primary cart">
            ADD TO CART
        </button>`
    }
    localStorage.clear()
}






