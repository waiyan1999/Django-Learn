
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


const categorTBody = document.getElementById("categoryTBody");
const productTBody = document.getElementById("productTBody");
const cartTBody = document.getElementById("cartTBody");
const cartItemTBody = document.getElementById("cartItemTBody");

const category_url = `/api/category/`;
const product_url = `/api/product/`;
const cart_url = `/api/cart/`;
const cartItem_url = `/api/cartItem/`;

//List Category
function listCategory() {
    console.log("function listCategory called");
    fetch(category_url, {
        method: "GET"
    })
    .then(response => response.json())
    .then(data => {
        console.log( "category", data)
        categorTBody.innerHTML="";
        data.forEach(category => {

              categorTBody.innerHTML += `
        
        <tr>
        <td> ${category.id} </td>
         <td> ${category.name} </td>
          <td> ${category.created_at} </td>
           <td> ${category.edited_at} </td>
           <td>
            <button class="btn btn-outline-warning btn-sm" onclick="editCategory(${category.id})" >Edit</button>
            <button class="btn btn-outline-danger btn-sm"  onclick="deleteCategory(${category.id})" >Delete</button>
           </td>
           
           </tr>
        `;

        });
        
    })
    
    .catch(error => {
        console.error("Error fetching categories:", error);
    });
}


//Create Category
function createCategory(event){

    event.preventDefault();

    console.log("function createCategory called")

    const categoryNameInput = document.getElementById("categoryName");
    const categoryName = categoryNameInput.value;
    console.log(" categoryName ",categoryName);

    fetch(category_url,{
        method : "POST",
        headers : {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrftoken
        },
        body : JSON.stringify({
            name : categoryName
        })
    })

    .then(response => response.json())
     .then(category => {
        console.log(category)
        categoryNameInput.value = '';

        listCategory();
    })
    
}

// Delete Category
function deleteCategory(categoryID){
    const categoryDeatil_url = `/api/category-detail/${categoryID}/`;

    console.log("function deleteCategory called");

    fetch(categoryDeatil_url,{
        method : "DELETE",
        headers : {
            "Content-Type":"application/json",
            "X-CSRFToken": csrftoken
        }
    })
    .then ( response => {
        console.log(response);
        if(response.ok){
            listCategory();
        }
        else{
            console.log("Delete Fail");
        }
    })
    .catch(error => {
        console.log("Error deleting categroy :" , error )
    })

    
}

//Edit Category
function editCategory(categoryID){
    const categoryDeatil_url = `/api/category-detail/${categoryID}/`;

    console.log('function editCategory called');
    console.log(categoryID)

    var updateName = prompt("Edit Category :" )
    console.log(updateName);
    

    fetch(categoryDeatil_url,{
        method : "PUT",
        headers : {
            "Content-Type":"application/json",
            "X-CSRFToken": csrftoken
        },
        body : JSON.stringify({
            name : updateName
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        listCategory();
        loadCategoryForDropdown();
    })
    .catch(error => {
        console.log("Error editing category ", error )
    })
    
}


// List Product
function listProduct(){
    console.log("function listProduct called")

    fetch(product_url,{
        method : "GET",
        headers : {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log( "product", data)
        productTBody.innerHTML="";
        data.forEach(product => {
            productTBody.innerHTML += `

            <tr>
            <td> ${product.id} </td>
            <td> ${product.category} </td>
            <td> ${product.name} </td>
            <td> ${product.price} </td>
            <td> ${product.stock} </td>
            <td> ${product.description} </td>
            <td> ${product.created_at} </td>
            <td> ${product.edited_at} </td>
            <td>
            <button class="btn btn-outline-success btn-sm" onclick="addToCart(event,${product.id})" >Add Cart</button>
            <button class="btn btn-outline-warning btn-sm" onclick="editProduct(${product.id})" >Edit</button>
            <button class="btn btn-outline-danger btn-sm"  onclick="deleteProduct(${product.id})" >Delete</button>
           </td>

            </tr>

            `;

        })
    })
}


//Load Categories into dropdrown
function loadCategoryForDropdown(){
    console.log("function loadCategoryForDropdown called");

    fetch(category_url,{
        method : "GET",
        headers : {
            "Content-Type":"application/json",
            "X-CSRFToken":csrftoken
        }
    })
    .then(response => response.json())
    .then(data => {

        console.log(data);
        const select = document.getElementById("productCateogry");
        console.log(select);
        select.innerHTML="";
        select.innerHTML= `<option value="">Seletct a Category </option>`;

        data.forEach(category => {


            const option = document.createElement('option');

            option.value = category.id;
            option.textContent = category.name;

            select.appendChild(option);


        });

    })
    .catch(error => {
        console.log("Error Occur",error)
    })
}


// Create Product
function createProduct(event){
    event.preventDefault();
    console.log("function createProduct called");

   
    const categorySelect = document.getElementById("productCateogry");
    const category = categorySelect.value;  // ✅ get selected value
    console.log("Selected category:", category);

    const name = document.getElementById("productName").value;
    const price = parseFloat(document.getElementById("productPrice").value);
    const stock = parseInt(document.getElementById("productStock").value);
    const description = document.getElementById("productDescription").value;
    
    console.log(name,price,stock,description);

    fetch(product_url,{
        method : "POST",
        headers : {
            "Content-Type":"application/json",
            "X-CSRFToken": csrftoken
    
        },
        body : JSON.stringify({
            category : category,
            name : name,
            price : price,
            stock : stock,
            description : description,
        })

    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        listProduct();
    })
    .catch(error => {
        console.log("Error Creating Product",error)
    })



}

//Delete Product
function deleteProduct(productID){
    const productDetail_url = `product-detail/${productID}/`;

    fetch(productDetail_url,{
        method : "DELETE",
        headers : {
            "Content-Type":"application/json",
            "X-CSRFToken": csrftoken
        }

    })
    .then(response => {
        console.log(response)

        if(response.ok){
            console.log("Successfully Deleted this product")
            listProduct();
        }
        else{
            console.log("Error occur")
        }
    })
    .catch(error => {
        console.log("Error Deleting Product ", error)
    })
}




//list Cart

function listCart(){

  fetch(cart_url, {
    method: 'GET',
    headers : {
      "Content-Type":"application/json",
      "X-CSRFToken" : csrftoken
    }
  })
  .then(response => response.json())
  .then(data => {
    console.log("Fetching Cart List")
    console.log(data)
     cartTBody.innerHTML='';
    data.forEach(cart => {
     

      const tr = document.createElement("tr");
      tr.innerHTML = ` 

              <td> ${cart.id} </td>
              <td> ${cart.created_at} </td>
        
              <td> 

                 
                 <button class="btn btn-outline-danger btn-sm" onclick="deleteCart(${cart.id})">Delete</button>
          

              </td>
      
      ` ;

      cartTBody.appendChild(tr);


    });
  });

}
    


// Create Cart
function addToCart(event,productID){
    event.preventDefault();

    let quantity = prompt("Enter product quantity :")
    if (quantity <= 0){
        alert('quantity must be grater than one');
    }
    console.log("Product Quantity :", quantity)

    fetch(cart_url,{
        method : "GET",
        headers : {
            "Content-Type":"application/json",
            "X-CSRFToken":csrftoken
        },
        
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if (data.length >0 ){
            cartID = data[0].id
            console.log("CartID:", cartID);
            createCartItem(cartID,productID,quantity);
        }
        else{
            console.log(data);
            console.log("No Cart Data");

            fetch(cart_url,{
                method : "POST",
                headers : {
                    "Content-Type":"application/json",
                    "X-CSRFToken":csrftoken
                },
                body : JSON.stringify({})
            })
            .then(response => response.json())
            .then(newData => {
                console.log("New Cart Data: ", newData );
                cartID = newData.id;
                listCart();
                createCartItem(cartID,productID,quantity);
                
            })
        }
    })


}


function listCartItem() {
  fetch(cartItem_url, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken
    }
  })
  .then(response => response.json())
  .then(data => {
    console.log("Fetching CartItem", data);

    const cartItemTable = document.getElementById("cartItemTable");
    cartItemTBody.innerHTML='';

    data.forEach(cartItem => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td>${cartItem.id}</td>
        <td>${cartItem.cart}</td>
        <td>${cartItem.product}</td>
        <td>${cartItem.quantity}</td>
        <td>
          <button class="btn btn-outline-warning btn-sm" onclick="editCartItem(${cartItem.id})">Edit</button>
          <button class="btn btn-outline-danger btn-sm" onclick="deleteCartItem(${cartItem.id})">Delete</button>
        </td>
      `;
      cartItemTBody.appendChild(tr);
    });
  })
  .catch(error => {
    console.error("Error fetching cart items:", error);
  });
}

function createCartItem(cartID,productID,quantity){

  fetch(cartItem_url,{
    method : "POST",
    headers : {
      "Content-Type":"application/json",
      "X-CSRFToken": csrftoken
    },
    body : JSON.stringify({
      cart : cartID,
      product : productID,
      quantity : quantity

    })

  })
  .then (response => response.json())
  .then(CartItemData => {
    console.log("New Cart Item Creted");
    console.log( "CartItem", CartItemData);
    listCartItem();

  })


}































document.addEventListener("DOMContentLoaded", function () {
    console.log("Page loaded");
    listCategory();
    loadCategoryForDropdown();
    listProduct();
    listCart();
    listCartItem();
});


