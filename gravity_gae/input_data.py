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
    G = nx.read_adjlist(dataset,
                        delimiter='\t',
                        create_using=nx.DiGraph())
    print("Ordering nodes...")
    ordering = list(G.nodes())
    adj = nx.adjacency_matrix(G, nodes_list = ordering)
    features = sp.identity(adj.shape[0])

    print("Data reading complete.")
    return adj, features, ordering