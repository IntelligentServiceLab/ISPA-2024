import argparse


def ParseArgs():
    parser = argparse.ArgumentParser(description='Model Params')
    parser.add_argument('--lr', default=0.001, type=float, help='learning rate')
    parser.add_argument('--batch', default=4096, type=int, help='batch size')
    parser.add_argument('--leaky', default=0.5, type=float, help='slope of leaky relu')
    parser.add_argument('--tstBat', default=64, type=int, help='number of users in a testing batch')
    parser.add_argument('--data', default='programmableweb', type=str, help='name of dataset')
    parser.add_argument('--hypergraphs_num', default=2, type=int, help='number of hypergraphs')
    parser.add_argument('--hyperNum', default=256, type=int, help='number of hyperedges')
    parser.add_argument('--att_head', default=2, type=int, help='number of attention heads')
    parser.add_argument('--keepRate', default=0.5, type=float, help='ratio of edges to keep')
    parser.add_argument('--ssl1_reg', default=3, type=float, help='weight for ssl loss')
    parser.add_argument('--ssl2_reg', default=3, type=float, help='weight for ssl loss')
    parser.add_argument('--edgeSampRate', default=0.1, type=float, help='Ratio of sampled edges')
    parser.add_argument('--temp', default=1, type=float, help='temperature')
    parser.add_argument('--epoch', default=120, type=int, help='number of epochs')
    parser.add_argument('--latdim', default=128, type=int, help='embedding size')
    parser.add_argument('--topk', default=20, type=int, help='top K')
    parser.add_argument('--reg', default=3e-8, type=float, help='weight decay regularizer')
    parser.add_argument('--decay', default=0.96, type=float, help='weight decay rate')
    parser.add_argument('--gcn_hops', default=2, type=int, help='number of hops in gcn precessing')
    parser.add_argument('--mult', default=1, type=float, help='multiplication factor')
    parser.add_argument('--load_model', default=None, help='model name to load')
    parser.add_argument('--save_path', default='tem', help='file name to save model and training record')
    parser.add_argument('--tstEpoch', default=3, type=int, help='number of epoch to test while training')
    parser.add_argument('--gpu', default='2', type=str, help='indicates which gpu to use')
    return parser.parse_args()


args = ParseArgs()
