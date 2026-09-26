import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import ContradictionDetectionBeliefUpdaterClient

def main():
    client = ContradictionDetectionBeliefUpdaterClient()
    res = client.resolve_belief_contradiction()
    print("=== Contradiction Detection Belief Updater Output ===")
    print(f"Entity: {res['entity_key']} | Contradiction Detected: {res['contradiction_detected']}")
    print(f"Historical: {res['historical_belief']}")
    print(f"New Claim:   {res['new_observed_claim']}")
    print(f"Verdict:     {res['resolution_verdict']}")
    print(f"Active State: {res['current_active_belief_state']} (Confidence: {res['epistemic_confidence']*100}%)")
    print(f"Action:      {res['recommended_graph_action']}")

if __name__ == '__main__':
    main()
