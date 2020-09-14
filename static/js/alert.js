async function show_alert(alert_box) {
    alert_box.classList.toggle('fade');
        await new Promise(r => setTimeout(r, 2000));
        alert_box.classList.toggle('fade');
}