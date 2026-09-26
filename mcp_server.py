import json, sys
from client import ContradictionDetectionBeliefUpdaterClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "contradiction-detection-belief-updater", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "resolve_belief_contradiction", "description": "Resolves epistemic contradictions between historical memory entries and newly observed agent facts."}]}}
    elif method == "tools/call":
        client = ContradictionDetectionBeliefUpdaterClient()
        res = client.resolve_belief_contradiction()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = ContradictionDetectionBeliefUpdaterClient()
        print(json.dumps(client.resolve_belief_contradiction(), indent=2))
