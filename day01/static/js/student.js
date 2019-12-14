function del(id) {
    //请求后台资源
    //请求方式：1.表单，2.get方式/a链接，3.ajax，
}
$(function () {
    //编辑学生信息
    let edit = $('.edit');
    edit.click(function () {
        //读取表中数据
        let tr = $(this).parents('tr');
        let children = tr.children('td');
        $('.ed-box').fadeIn();
        let id =children.eq(0).text();
        $('#up').attr('sid',id)
        $('[name=idcard]').val(children.eq(1).text());
        $('[name=name]').val(children.eq(2).text());
        $('[name=age]').val(children.eq(3).text());
        if( children.eq(4).attr('val')=='1'){
            console.log(123)
            $('[name=sex]').eq(0).attr('checked','checked')
        }else{
            console.log(456)
            $('[name=sex]').eq(1).attr('checked','checked')
        }
        $('[name=class]').val(children.eq(5).text());
        console.log(children.eq(4).attr('val'))


    })
    $('#up').click(function () {
        $.ajax({
            url:'edit',
            type:'post',
            data:{
                id:$('#up').attr('sid'),
                idcard:$("[name='idcard']").val(),
                name:$("[name=name]").val(),
                age:$("[name=age]").val(),
                sex:$("[name=sex]").val(),
                class:$("[name=class]").val(),
            },
            success:function (data) {
                console.log(data)
                $('.ed-box').fadeOut();
            },
            error:function (e) {
                console.log(e)
            }
        })
    })
})
