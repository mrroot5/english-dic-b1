(function() {
    function initMaterialize() {
        $(".button-collapse").sideNav();
        $('select').material_select();
    }

    function main() {
        initMaterialize();

        $.fn.dataTable.ext.classes.sPageButton = 'btn';

        $('.datatables').DataTable({
            responsive: true,
            paging: false,
            dom: 'Bfrtip',
            buttons: [
                { extend: 'excel', className: 'waves-effect btn' },
                { extend: 'csv', className: 'waves-effect btn' },
                { extend: 'pdf', className: 'waves-effect btn' },
                { extend: 'print', className: 'waves-effect btn' }
            ],
            initComplete: function(settings, json) {
                $("button").removeClass("dt-button buttons-excel buttons-html5");
                $("button").removeClass("buttons-csv");
                $("button").removeClass("buttons-pdf");
                $("button").removeClass("buttons-print");
                $("button").removeClass("paginate_button");
            }
        });
    }



    $(document).ready(function() {
        main();
    });
}());
