from src.train import train_model


def test_train_model_returns_good_metrics():
    model, metrics = train_model(n_estimators=10, max_depth=3)
    assert model is not None
    assert 0.8 <= metrics["accuracy"] <= 1.0
    assert 0.8 <= metrics["f1_score"] <= 1.0
