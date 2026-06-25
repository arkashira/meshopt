import pytest
from alerts import AlertManager, AlertRule, Alert

def test_create_alert_rule():
    manager = AlertManager()
    rule = manager.create_alert_rule("metric", 10.0, "Slack", "https://slack.com")
    assert rule.id == 1
    assert rule.metric == "metric"
    assert rule.threshold == 10.0
    assert rule.notification_channel == "Slack"
    assert rule.notification_url == "https://slack.com"

def test_edit_alert_rule():
    manager = AlertManager()
    rule = manager.create_alert_rule("metric", 10.0, "Slack", "https://slack.com")
    edited_rule = manager.edit_alert_rule(rule.id, metric="new_metric")
    assert edited_rule.metric == "new_metric"

def test_delete_alert_rule():
    manager = AlertManager()
    rule = manager.create_alert_rule("metric", 10.0, "Slack", "https://slack.com")
    manager.delete_alert_rule(rule.id)
    assert len(manager.alert_rules) == 0

def test_trigger_alert():
    manager = AlertManager()
    rule = manager.create_alert_rule("metric", 10.0, "Slack", "https://slack.com")
    alert = manager.trigger_alert(rule.id, "severity")
    assert alert.id == 1
    assert alert.rule_id == rule.id
    assert alert.timestamp
    assert alert.severity == "severity"

def test_get_alerts():
    manager = AlertManager()
    rule = manager.create_alert_rule("metric", 10.0, "Slack", "https://slack.com")
    alert = manager.trigger_alert(rule.id, "severity")
    alerts = manager.get_alerts()
    assert len(alerts) == 1
    assert alerts[0].id == alert.id

def test_get_alert_rule():
    manager = AlertManager()
    rule = manager.create_alert_rule("metric", 10.0, "Slack", "https://slack.com")
    retrieved_rule = manager.get_alert_rule(rule.id)
    assert retrieved_rule.id == rule.id
