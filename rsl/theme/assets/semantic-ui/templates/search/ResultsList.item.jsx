/*
 *   Copyright (C) 2021 RSL.
 *
 * rsl is free software; you can redistribute it and/or modify it under the
 * terms of the MIT License; see LICENSE file for more details.
 */

import React from "react";
import { Item, List } from "semantic-ui-react";

const rslResultsListItem = ({ result, index }) => {
  const contributors = result.metadata.contributors || [];
  return (
    <Item key={index} href={`/records/${result.id}`}>
      <Item.Content>
        <Item.Header>{result.metadata.title}</Item.Header>
        <Item.Description>
          {contributors && (
            <List horizontal relaxed>
              {contributors.map((contributor, idx) => (
                <List.Item key={idx}>{contributor.name}</List.Item>
              ))}
            </List>
          )}
        </Item.Description>
      </Item.Content>
    </Item>
  );
};

export default rslResultsListItem;



