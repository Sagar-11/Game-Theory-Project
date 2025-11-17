import json
import os
import networkx as nx
from z3 import Sum, is_expr


def runExperiments(graph, solution, resultsFile):
    """ 
    Calculates metrics (Revenue, Average Cost) from the solved graph/solution 
    and appends them to the resultsFile under the "metrics" key.
    """
    # --- 1. Initialize data structure and check solution ---
    if solution is None:
        print("Skipping experiment: Solution is null.")
        return
    
    if os.path.exists(resultsFile):
        with open(resultsFile, 'r') as f:
            data = json.load(f)
    else:
        data = {"metrics": {"revenue": [], "avg_cost": []}}
    
    total_revenue = 0.0
    total_cost_sum = 0.0
    total_flow = 0.0
    
    # Calculate Total Revenue and Total Flow
    for u, v, key, edge_data in graph.edges(keys=True, data=True):
        # Extract solved flow (f_e) and price.
        f_e = edge_data.get('f_e')
        price = edge_data.get('price')
        k = edge_data.get('k', 2) # Use 2.0 if k is missing

        # Calculate revenue for this edge (f_e * price)
        if not (is_expr(price) or is_expr(f_e)):
            edge_revenue = k*f_e + price
            total_revenue += edge_revenue
            # Total flow (sum of all f_e)
            total_flow += f_e
        
    
    # Note: Objective value F is Total Cost, where Cost_R = sum_e_in_R ((e.k)f_e + e.price)
    objective_val = float(solution['objective_val'].as_long()) 
    
    total_cost_sum = objective_val
    avg_cost = total_cost_sum / total_flow
        
    # Append the calculated metrics
    data['metrics']['revenue'].append(total_revenue)
    data['metrics']['avg_cost'].append(avg_cost)
    
    # Save the updated JSON data
    with open(resultsFile, 'w') as f:
        json.dump(data, f, indent=4)
