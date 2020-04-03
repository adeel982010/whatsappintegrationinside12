odoo.define('eldo_customization.balance_history', function (require) {
"use strict";
    
    var AbstractAction = require('web.AbstractAction');
    var ControlPanelMixin = require('web.ControlPanelMixin');
    var core = require('web.core');
    var framework = require('web.framework');
    var rpc = require('web.rpc');
    var QWeb = core.qweb;
    var _t = core._t;

    var BalanceHistory = AbstractAction.extend(ControlPanelMixin, {
        title: _t('Balance History'),
        template: 'BalanceHistoryView',
        events: {
            'click button.search_history': '_onSearchHistoryClicked',
        },
        init: function (parent, params) {
            var self = this;
            self._super.apply(self, arguments);
            self.record_id = params.context.active_id;
        },
        renderElement: function () {
            var self = this;
            self._super.apply(self, arguments);
            if (! self.record_id){
                window.location.href = '/';
            }
            setTimeout(function (){
                $('.load-body').hide();
                $('.cbal').html('');
            }, 0);
        },
        _onSearchHistoryClicked: function() {
            var self = this;
            $('.main-body').html('');
            $('.cbal').html('');
            $('.load-body').hide();
            if ($('.start_date').val() && $('.end_date').val()){
                framework.blockUI();
                rpc.query({
                    model: 'e.wallet',
                    method: 'get_balance_history',
                    args: [
                        self.record_id,
                        $('.start_date').val(),
                        $('.end_date').val(),
                    ],
                }).always(function(){
                    framework.unblockUI();
                }).then(function (res) {
                    if (res){
                        if (res.error){
                            self.do_warn(_t('Error'), res.error);
                        }
                        else if(res.success){
                            $('.load-body').show();
                            if (res.success.transactionlog && res.success.transactionlog.transaction && res.success.cbal){
                                var transactions = _.sortBy(res.success.transactionlog.transaction, 'tdate').reverse();
                                var $content = QWeb.render('HistoryRowView', {
                                    history_lines: transactions
                                });
                                $('.cbal').html("<div class=history-border>R "+res.success.cbal+"</div>");
                                $('.main-body').html($content);
                            }
                        }
                    }
                })
            }
            else{
                self.do_warn(_t('Error'), 'Please select start date and end date !!');
            }
        },
    });

    core.action_registry.add('open_balance_history', BalanceHistory);
    return {
        BalanceHistory : BalanceHistory,
    };

});