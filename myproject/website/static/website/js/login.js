setTimeout(function () {
    const alerts = document.querySelectorAll('.message-alert');
    alerts.forEach(function(alert) {
        alert.remove();
    });
}, 3000);