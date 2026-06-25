import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class AlertRule:
    id: int
    metric: str
    threshold: float
    notification_channel: str
    notification_url: str

@dataclass
class Alert:
    id: int
    rule_id: int
    timestamp: datetime
    severity: str

class AlertManager:
    def __init__(self):
        self.alert_rules = []
        self.alerts = []

    def create_alert_rule(self, metric: str, threshold: float, notification_channel: str, notification_url: str) -> AlertRule:
        rule_id = len(self.alert_rules) + 1
        rule = AlertRule(rule_id, metric, threshold, notification_channel, notification_url)
        self.alert_rules.append(rule)
        return rule

    def edit_alert_rule(self, rule_id: int, metric: str = None, threshold: float = None, notification_channel: str = None, notification_url: str = None) -> AlertRule:
        for rule in self.alert_rules:
            if rule.id == rule_id:
                if metric:
                    rule.metric = metric
                if threshold:
                    rule.threshold = threshold
                if notification_channel:
                    rule.notification_channel = notification_channel
                if notification_url:
                    rule.notification_url = notification_url
                return rule
        raise ValueError("Alert rule not found")

    def delete_alert_rule(self, rule_id: int) -> None:
        self.alert_rules = [rule for rule in self.alert_rules if rule.id != rule_id]

    def trigger_alert(self, rule_id: int, severity: str) -> Alert:
        alert_id = len(self.alerts) + 1
        alert = Alert(alert_id, rule_id, datetime.now(), severity)
        self.alerts.append(alert)
        return alert

    def get_alerts(self) -> List[Alert]:
        return self.alerts

    def get_alert_rule(self, rule_id: int) -> AlertRule:
        for rule in self.alert_rules:
            if rule.id == rule_id:
                return rule
        raise ValueError("Alert rule not found")
