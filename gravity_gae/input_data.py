import networkx as nx
import scipy.sparse as sp

def load_data(dataset):
    """ Load datasets from text files

    :param dataset: 'cora', 'citeseer' or 'google' graph dataset.
    :return: n*n sparse adjacency matrix and n*f node-level feature matrix

    Note: in this paper, all three datasets are assumed to be featureless.
    As a consequence, the feature matrix is the identity matrix I_n.
    """
    print("Reading adjacency list...")
    node_map = {}
    edge_index = [[],[]]
    node_index=0
    with open(dataset) as adjlist:
        for row in adjlist:
            row = row.split('\t')
            source = row[0]
            if source not in node_map.keys():
                node_map[source] = node_index
                node_index +=1
            for target in row[1:]:
                if target not in node_map.keys():
                    node_map[target] = node_index
                    node_index+=1
                edge_index[0].append(node_map[source])
                edge_index[1].append(node_map[target])
    
    nNodes = len(node_map.keys())
    adj = sp.coo_matrix(
        (
            np.ones(len(edge_index[0])), 
            (edge_index[0], edge_index[1])
        ), 
        shape=(nNodes, nNodes))
    features = sp.identity(adj.shape[0])

    print("Data reading complete.")
    return adj, features, node_map