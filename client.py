from __future__ import print_function
import logging

import grpc

# import the generated classes
import poisson_predictor_pb2
import poisson_predictor_pb2_grpc


def run():
    # open a gRPC channel
    with grpc.insecure_channel("localhost:50051") as channel:

        # create a stub (client)
        stub = poisson_predictor_pb2_grpc.PoissonPredictorStub(channel)

        # create a valid request message
        pair_scores_request = poisson_predictor_pb2.PairScoresRequest(
            ave_home_scored=2.3333333, ave_away_scored=0.6666667
        )

        # make the call
        response = stub.PredictOnAvePairScores(pair_scores_request)
        print(response.odds)


if __name__ == "__main__":
    logging.basicConfig()
    run()
