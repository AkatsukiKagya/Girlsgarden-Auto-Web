# 状态机



```mermaid
stateDiagram-v2
    [*] --> HOME

    HOME --> SORTIE : 点击出击
    SORTIE --> BATTLE : 点击战斗
    BATTLE --> BATTLE_RESULT : 战斗结束
    BATTLE_RESULT --> REWARD : 进入结算
    REWARD --> HOME : 返回主页
```

