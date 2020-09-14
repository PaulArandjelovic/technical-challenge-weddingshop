function networkRequest(arg, product_id, qty) {
    httpRequest = new XMLHttpRequest();

    if (!httpRequest) {
      alert('Giving up :( Cannot create an XMLHTTP instance');
      return false;
    }

    httpRequest.onreadystatechange = alertContents;

    if (arg === "gen_prod_table") {
        httpRequest.open('GET', '/request_manager/gen_prod_table', false);
    }
    else if (arg === "gen_checkout_table") {
        httpRequest.open('GET', '/request_manager/gen_checkout_table', false);
    }
    else if (arg === "add_list_item") {
        httpRequest.open('GET', '/request_manager/add_list_item?p_id='
            + product_id + '&qty=' + qty, false);
    }
    else if (arg === "remove_list_item") {
        httpRequest.open('GET', '/request_manager/remove_list_item?p_id='
            + product_id, false);
    }


    httpRequest.send();
  return httpRequest.responseText;
}


function alertContents() {
    if (httpRequest.readyState === XMLHttpRequest.DONE) {
      if (httpRequest.status === 200) {
        return httpRequest.responseText;
      } else {
        alert('There was a problem with the request.');
      }
    }
  }